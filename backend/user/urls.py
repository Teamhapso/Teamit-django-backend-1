from django.urls import path

from .views import *

urlpatterns = [
     # user
     path("", UserWithProfileCreateAPIView.as_view()),
     path("<int:pk>/", UserDetailAPIView.as_view()),
     path("name/available/", CheckUserNameAvailability.as_view()),

     # user profile
     path("profiles/", UserWithProfileListAPIView.as_view()),
     path("<int:pk>/profile/", UserWithProfileRetrieveUpdateAPIView.as_view()), 
     
     path("send-friend-request/", SendFriendRequestAPIView.as_view()),
     path("accept-friend-request/", AcceptFriendRequestAPIView.as_view()),
     path("decline-friend-request/", DeclineFriendRequestAPIView.as_view()),
     path("friends/", UserFriendsListAPIView.as_view()),
     
     # likes
     path("<int:pk>/like/", LikeUnlikeAPIView.as_view()),
     path("likes/", UserLikesListAPIView.as_view()),
]
