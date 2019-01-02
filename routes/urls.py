from django.conf.urls import url

from routes import views

urlpatterns = [
    url(r'^home/', views.TestAPI.as_view(), name='get-home-page-data'),
    url(r'^get-directions/', views.DirectionsAPI.as_view(), name='directions'),
]
