from django.urls import path

from .views import *

urlpatterns = [
     path("team/", TeamNotificationListAPIView.as_view()),
     path("", NotificationListAPIView.as_view()),
     path("unread/status/", UnreadNotificationsStatusAPIView.as_view()),
     
]
