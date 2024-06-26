from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from django.db import transaction

from .models import *
from .serializers import *
from user.models import User
from team.models import Team

class ReportUserOrTeamAPIView(generics.CreateAPIView):
     serializer_class = ReportDetailSerializer
     
     @transaction.atomic
     def create(self, request, *args, **kwargs):
          user = request.user
          
          reported_type = request.data.get('reported_type', None)
          block = request.data.pop('block', None)
          
          # handle exceptions and block team/user
          if reported_type == 'team':
               reported_team_pk = request.data.get('reported_team', None)
               reported_team = get_object_or_404(Team, pk=reported_team_pk)
               
               # abort if user is team's creator
               if user == reported_team.creator:
                    raise PermissionDenied("User is not allowed to report this team. user is creator of team.")
          
               # block team 
               if block:
                    user.blocked_teams.add(reported_team)
               
          elif reported_type == 'user':
               reported_user_pk = request.data.get('reported_user', None)
               reported_user = get_object_or_404(User, pk=reported_user_pk)
               
               # abort if reported user is reporter
               if user == reported_user:
                    return Response({"detail": "user cannot report oneself"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
               
               # block user
               if block:
                    user.blocked_users.add(reported_user)
     
          elif reported_type == 'team_post':
               reported_team_post_pk = request.data.get('reported_team_post', None)
               team_post = get_object_or_404(TeamPost, pk=reported_team_post_pk)
               
               # abort if reported writer is reporter
               if user.pk == team_post.writer.user.pk:
                    return Response({"detail": "user cannot report oneself"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
               
               # block writer(user)
               if block:
                    user.blocked_users.add(team_post.writer.user)
                
          elif reported_type == 'team_post_comment':
               reported_team_post_comment_pk = request.data.get('reported_team_post_comment', None)
               team_post_comment = get_object_or_404(TeamPostComment, pk=reported_team_post_comment_pk)
               
               # abort if reported writer is reporter
               if user.pk == team_post_comment.writer.user.pk:
                    return Response({"detail": "user cannot report oneself"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
               
               # block writer(user)
               if block:
                    user.blocked_users.add(team_post_comment.writer.user)
          
          # add user instance to request data
          request.data['reporter'] = user.pk
          
          # create report
          serializer = self.get_serializer(data=request.data)
          serializer.is_valid(raise_exception=True)
          report = serializer.save()
          
          return Response(serializer.data, status=status.HTTP_201_CREATED)