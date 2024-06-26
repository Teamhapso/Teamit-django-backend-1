from django.urls import path

from .views import *

urlpatterns = [
     path("", DeviceListCreateView.as_view(), name='create / list device'),
     path("token/", DeviceDetailView.as_view(), name='retrieve, update, delete device'),
]
