
from rest_framework import status, generics
from rest_framework.permissions import AllowAny
from django.shortcuts import render_to_response
from rest_framework.response import Response
import googlemaps
import json, time
from datetime import datetime
from forecastiopy import *

# from api import utils as api_utils
from routes import utils as weather_utils
from routes import models as weather_models

gmaps = googlemaps.Client(key='xxxxxx')
darksky_api_key = 'xxxxxx'

# Create your views here.

class TestAPI(generics.GenericAPIView):
    """
    API to load the home page
    """
    permission_classes = (AllowAny, )

    def get(self, request):
        """
        Loading the home page for the application
        """
        return render_to_response('index.html')


class DirectionsAPI(generics.GenericAPIView):
    """
    API to get the weather data
    """
    permission_classes = (AllowAny, )

    def get(self, request):
        """
        Getting weather data from the external APIs or the database
        """

        data = request.query_params.dict()
        start_time = time.time()

        # Database call
        old_data = weather_models.DirectionsData.objects.filter(origin=data['origin'], destination=data['destination'],
                                                                travel_mode=data['travelMode']).last()
        print('Database call takes %s'%(time.time() - start_time))

        # Check if directions data is present in the database
        if old_data:
            directions_result = old_data.routes_response
            print(old_data.modified_at)

            # Check if the request is made on the same day
            if old_data.modified_at.date() == datetime.now().date():
                cities_lat_lng_list = old_data.route_weather_data
            else:
                cities_lat_lng_list = []
                print(old_data.route_cities_data)
                for city in old_data.route_cities_data:
                    fio = ForecastIO.ForecastIO(darksky_api_key,
                                                lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                                                latitude=city['lat'], longitude=city['lng'])
                    currently = FIOCurrently.FIOCurrently(fio)
                    cities_lat_lng_list.append({'city': city['city'], 'temp': currently.temperature,
                                                'icon': currently.icon, 'lat': city['lat'], 'lng': city['lng']})
                old_data.route_weather_data = cities_lat_lng_list
                old_data.save()

        else:
            # Directions data is not available
            start_time = time.time()
            directions_result = gmaps.directions(data['origin'], data['destination'], mode=data['travelMode'])
            directions_time = time.time() - start_time
            lat_lng_list = weather_utils.get_weather_data(directions_result)

            cities_lat_lng_list = []
            cities_list = []
            cities_lat_lng_data = []
            reverse_geocoding_time = 0.0
            weather_api_time = 0.0
            for coord in lat_lng_list:
                start_time = time.time()
                reverse_geocode_result = gmaps.reverse_geocode((coord['lat'], coord['lng']))
                reverse_geocoding_time += time.time() - start_time
                for result in reverse_geocode_result:
                    if 'locality' in result['types']:
                        if result['formatted_address'] not in cities_list:
                            start_time = time.time()
                            fio = ForecastIO.ForecastIO(darksky_api_key,
                                                        lang=ForecastIO.ForecastIO.LANG_ENGLISH,
                                                        latitude=coord['lat'], longitude=coord['lng'])
                            weather_api_time += time.time() - start_time
                            currently = FIOCurrently.FIOCurrently(fio)
                            cities_lat_lng_list.append({'city': result['formatted_address'],
                                                        'temp': currently.temperature,
                                                        'icon': currently.icon,
                                                        'lat': coord['lat'], 'lng': coord['lng']})
                            cities_list.append(result['formatted_address'])
                            cities_lat_lng_data.append({'city': result['formatted_address'], 'lat': coord['lat'],
                                                        'lng': coord['lng']})
            google_time = reverse_geocoding_time + directions_time
            print('Google call takes %s' % google_time)
            print('Dark Sky call takes %s' %weather_api_time)
            dir_obj = weather_models.DirectionsData.objects.create(origin=data['origin'],
                                                                   destination=data['destination'],
                                                                   travel_mode=data['travelMode'],
                                                                   routes_response=directions_result,
                                                                   route_weather_data=cities_lat_lng_list,
                                                                   route_cities_data=cities_lat_lng_data)
        directions = {'routes': directions_result, 'weather_data': cities_lat_lng_list}
        return Response(data=json.dumps(directions), status=status.HTTP_200_OK)
