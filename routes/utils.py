from routes import constants as routes_constants
from routes.exceptions import GenericException


def get_weather_data(directions_result):
    """
    Only add waypoints if distance from the previous waypoint for which weather data is to be shown is at least 10000
    metres away
    """
    steps = directions_result[0]['legs'][0]['steps']
    lat_lng_list = []
    if len(steps) == 0:
        # If there is no data available throw an exception
        raise GenericException(exception_code=NONRETRYABLE_CODE["BAD_REQUEST"],
                               detail='No data present in routes', request=None)
    distance = 0
    dest = steps[len(steps)-1]
    for step in steps:
        if distance == 0:
            lat_lng_list.append({'lat': step['start_location']['lat'],
                                 'lng': step['start_location']['lng']})
            distance += step['distance']['value']
        else:
            distance += step['distance']['value']
            if distance > routes_constants.DISTANCE_RESET_CONSTANT:
                distance = 0
    lat_lng_list.append({'lat': dest['start_location']['lat'],
                         'lng': dest['start_location']['lng']})
    return lat_lng_list
