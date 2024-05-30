import json

from channels.generic.websocket import AsyncWebsocketConsumer
from django.db.models import Sum, F
from channels.db import database_sync_to_async
from django.db import transaction
from rest_framework.exceptions import ValidationError

from .models import *
from .serializers import*
from .index import *
from . import client

class ChatStatusConsumer(AsyncWebsocketConsumer):
     # DB related functions
     @database_sync_to_async
     def fetch_private_chatrooms(self):
          blocked_users = self.user.blocked_users.values('pk')
          private_chatrooms = PrivateChatParticipant.objects.filter(
                    user=self.user
               ).exclude(
                    chatroom__participants__in=blocked_users
               ).distinct()
          room_list = MyPrivateChatRoomDetailSerializer(private_chatrooms, many=True).data
          return sorted(room_list, key=lambda x: x['updated_at'], reverse=True)

     @database_sync_to_async
     def fetch_inquiry_chatrooms(self):
          responder_rooms = InquiryChatRoom.objects.filter(team__permission__responder=self.user)
          inquirer_rooms = InquiryChatRoom.objects.filter(inquirer=self.user)
          responder_room_list = InquiryChatRoomDetailSerializer(responder_rooms, many=True, context={'user': self.user}).data
          inquirer_room_list = InquiryChatRoomDetailSerializer(inquirer_rooms, many=True, context={'user': self.user}).data
          if self.filter == 'responder':
               return responder_room_list
          elif self.filter == 'inquirer':
               return inquirer_room_list
          room_list = responder_room_list + inquirer_room_list
          return sorted(room_list, key=lambda x: x['updated_at'], reverse=True)
     
     @database_sync_to_async
     def fetch_team_chatrooms(self):
          team_chatrooms = TeamChatRoom.objects.filter(team__pk=self.team_id, participants=self.user)
          return TeamChatRoomDetailSerializer(team_chatrooms, many=True, context={'user': self.user}).data

     @database_sync_to_async
     def update_private_chatroom_alarm(self, chatroom_id):
          instance = PrivateChatParticipant.objects.filter(user=self.user, chatroom=chatroom_id).first()
          instance.alarm_on = not instance.alarm_on
          instance.save()
          
     @database_sync_to_async
     def update_inquiry_chatroom_alarm(self, chatroom_id):
          instance = InquiryChatRoom.objects.get(id=chatroom_id)
          type = 'inquirer'
          if self.user == instance.inquirer:
               instance.inquirer_alarm_on = not instance.inquirer_alarm_on
          else:
               type = 'responder'
               instance.responder_alarm_on = not instance.responder_alarm_on
          instance.save()
     
     @database_sync_to_async
     def update_team_chatroom_alarm(self, chatroom_id):
          instance = TeamChatParticipant.objects.filter(user=self.user, chatroom=chatroom_id).first()
          instance.alarm_on = not instance.alarm_on
          instance.save()
     
     @database_sync_to_async
     def get_total_unread_cnt(self):
          private_unread_cnt = PrivateChatParticipant.objects.filter(user=self.user).aggregate(private_unread_cnt=Sum('unread_cnt'))['private_unread_cnt'] or 0
          team_unread_cnt = TeamChatParticipant.objects.filter(user=self.user, member__isnull=False).aggregate(team_unread_cnt=Sum('unread_cnt'))['team_unread_cnt'] or 0
          inquirer_unread_cnt = InquiryChatRoom.objects.filter(inquirer=self.user).aggregate(inquiry_unread_cnt=Sum('inquirer_unread_cnt'))['inquiry_unread_cnt'] or 0
          responder_unread_cnt = InquiryChatRoom.objects.filter(team__permission__responder=self.user).aggregate(responder_unread_cnt=Sum('responder_unread_cnt'))['responder_unread_cnt'] or 0
          
          return private_unread_cnt + team_unread_cnt + inquirer_unread_cnt + responder_unread_cnt
     
     @database_sync_to_async
     @transaction.atomic
     def remove_user_from_chatroom(self, chat_type, chatroom_id):
          if chat_type == 'private':
               participant = PrivateChatParticipant.objects.get(user=self.user, chatroom=chatroom_id)
               participant_name = participant.user.name
               participant.delete()
               return participant_name, None
          if chat_type == 'team':
               participant = TeamChatParticipant.objects.get(user=self.user, chatroom=chatroom_id)
               participant_name = participant.name
               participant_position = participant.position
               participant.delete()
               return participant_name, participant_position
          if chat_type == 'inquiry':
               chatroom = InquiryChatRoom.objects.get(chatroom=chatroom_id)
               participant_name = ''
               if chatroom.inquirer == self.user:
                    participant_name = chatroom.inquirer.name
                    chatroom.inquirer = None
               else:
                    participant_name = chatroom.team.name
                    chatroom.team = None
               chatroom.save()
               return participant_name, None
          
     @database_sync_to_async
     @transaction.atomic
     def create_message(self, chat_type, data):
          if chat_type == 'private':
               pass
          if chat_type == 'team':
               try:
                    serializer = TeamMessageCreateSerialzier(data=data)
                    serializer.is_valid(raise_exception=True)
                    instance = serializer.save()
                    return TeamMessageSerializer(instance, context={'unread_cnt': None}).data
               except ValidationError as e:
                    self.send_message('error', e.detail)
          if chat_type == 'inquiry':
               pass
     
     commands = {
          'fetch_private_chatrooms': fetch_private_chatrooms,
          'fetch_inquiry_chatrooms': fetch_inquiry_chatrooms,
          'fetch_team_chatrooms': fetch_team_chatrooms,
          'update_private_chatroom_alarm': update_private_chatroom_alarm,
          'update_inquiry_chatroom_alarm': update_inquiry_chatroom_alarm,
          'update_team_chatroom_alarm': update_team_chatroom_alarm,
     }


     async def connect(self):
          self.user = self.scope.get('user')
          self.user_id = self.user.id
          self.name = f'status_{self.user_id}'
          self.chat_type = 'all'
          self.team_id = 0
          self.filter = 'all'
          # self.unread_cnt = await self.get_unread_cnt()
          self.total_unread_cnt = await self.get_total_unread_cnt()

          await self.channel_layer.group_add(self.name, self.channel_name)
          await self.accept()
          
     async def disconnect(self, close_code):
          await self.channel_layer.group_discard(self.name, self.channel_name)
          await self.close(code=close_code)

     async def receive(self, text_data):
          try:
               data = json.loads(text_data)
          except json.JSONDecodeError:
               await self.close()
          
          msg_type = data.get("type")
          
          if msg_type == 'change':
               await self.handle_change(data)
          elif msg_type == 'udpate_alarm_status':
               await self.handle_update_alarm_status(data)
          elif msg_type == 'exit':
               await self.handle_exit(data)
          elif msg_type == 'search':
               await self.handle_search(data)
     
     #-------------------handle reltaed--------------------------
     async def handle_change(self, data):
          self.chat_type = data.get("chat_type", self.chat_type)
          self.team_id = data.get("team_id", self.team_id)
          self.filter = data.get("filter", self.team_id)
          
          if self.chat_type == 'all':
               await self.send_message('update_total_unread_cnt', {'cnt': self.total_unread_cnt})
          else:
               await self.send_chatroom_list(self.chat_type)

     async def handle_update_alarm_status(self, data):
          chat_type = data.get('chat_type')
          chatroom_id = data.get('chatroom_id')
          if chat_type and chatroom_id:
               await self.commands[f'update_{chat_type}_chatroom_alarm'](self, chatroom_id)
     
     async def handle_exit(self, data):
          chat_type = data.get('chat_type')
          chatroom_id = data.get('chatroom_id')
          if chat_type and chatroom_id:
               # create exit message
               name, position = await self.remove_user_from_chatroom(chat_type, chatroom_id)
               data = {
                    'chatroom': chatroom_id,
                    'content': f'{name} / {position} 님이 퇴장했습니다' if position else f'{name} 님이 퇴장했습니다',
                    'is_msg': False
               }
               message = await self.create_message(chat_type, data)
               
               # send message to group
               chatroom_name = f'{chat_type}_chat_{chatroom_id}'
               await self.channel_layer.group_send(
                    chatroom_name, {"type": "msg", "message": message}
               )
               await self.close()

     async def handle_search(self, data):
          self.chat_type = 'all'
          query = data.get('query', '')
          results = {
               'private': await self.private_chatroom_search(query),
               'team': await self.team_chatroom_search(query), 
               'inquiry': await self.inquiry_chatroom_search(query)
          }
          
          await self.send_message('search_results', results)
          
     #-------------------event related----------------------------
     async def msg(self, event):
          chat_type = event['chat_type']
          message = event['message']
          update_unread_cnt = message.get('update_unread_cnt', False)
          team_id = event.get('team_id', self.team_id)
          filter = event.get('filter', self.filter)
          
          if update_unread_cnt:
               self.total_unread_cnt += 1
     
          if self.chat_type == 'all':
               await self.send_message('update_total_unread_cnt', {'cnt': self.total_unread_cnt})
               await self.send_update_message(chat_type, message)
          elif self.chat_type == chat_type and self.team_id == team_id and (self.filter in (filter, 'all')):
               await self.send_update_message(chat_type, message)
               
     #--------------------utiity related---------------------------------       
     async def send_message(self, type, message):
          await self.send(text_data=json.dumps({
               'type': type,
               'message': message
          }))
     
     async def send_update_message(self, chat_type, message):
          await self.send(text_data=json.dumps({
               'type': 'update_chatroom',
               'chat_type': chat_type,
               'message': message
          }))
     
     async def send_chatroom_list(self, chat_type):
          type = f'{chat_type}_chatroom_list'
          message = await self.commands[f'fetch_{chat_type}_chatrooms'](self)
          await self.send_message(type, message)
     
     #------------------- DB related-------------------------------
     @database_sync_to_async
     def private_chatroom_search(self, query):
          blocked_users = self.user.blocked_users.values('pk')
          filter_expression = f'user_pk={self.user.pk}'
          exclude_expression = ' OR '.join([f'NOT other_user_pk:{blocked_user}' for blocked_user in blocked_users])
          filter_expression += f' AND {exclude_expression}' if exclude_expression else ''
          results = client.perform_search(query, 'private', filter_expression)
          return results

     @database_sync_to_async
     def team_chatroom_search(self, query):
          filter_expression = f'user_pk={self.user.pk}'
          results = client.perform_search(query, 'team', filter_expression)
          return results
     
     @database_sync_to_async
     def inquiry_chatroom_search(self, query):
          filter_expression = f'inquirer_pk={self.user.pk} OR responder_pk={self.user.pk}'
          results = client.perform_search(query, 'inquiry', filter_expression)
          chatrooms = InquiryChatRoom.objects.filter(pk__in=results)
          return InquiryChatRoomDetailSerializer(chatrooms, many=True, context={'user': self.user}).data
     
######################################################################
class TeamInquiryStatusConsumer(AsyncWebsocketConsumer):
     async def connect(self):
          self.user = self.scope.get('user')
          self.team_pk = int(self.scope["url_route"]["kwargs"]["team_pk"])
          self.chatroom_name = f"team_inquiry_status_{self.team_pk}"
          self.loaded_cnt = 0
          is_member = await self.get_team_and_check_members()
          if not is_member:
               await self.close()
               return
          await self.channel_layer.group_add(self.chatroom_name, self.channel_name)
          await self.accept()
          await self.send_chatroom_list()
          
     async def disconnect(self, close_code):
          await self.channel_layer.group_discard(self.chatroom_name, self.channel_name)
          await self.close(code=close_code)

     #-------------------event related----------------------------
     async def msg(self, event):
          message = event['message']
          await self.send_message('update_chatroom', message)  
               
     #--------------------utiity related---------------------------------       
     async def send_message(self, type, message):
          await self.send(text_data=json.dumps({
               'type': type,
               'message': message
          }))
          
     async def send_chatroom_list(self):
          type = f'team_inquiry_chatroom_list'
          message = await self.fetch_team_inquiry_chatroom_list()
          await self.send_message(type, message)
     
     #---------------------DB related-------------------------------
     @database_sync_to_async
     def get_team_and_check_members(self):
          self.team = Team.objects.get(pk=self.team_pk)
          return self.team.members.filter(pk=self.user.pk).exists()

     @database_sync_to_async
     def fetch_team_inquiry_chatroom_list(self):
          inquiry_chatrooms = self.team.inquiry_chat_rooms.all()
          return InquiryChatRoomDetailForTeamSerializer(inquiry_chatrooms, many=True).data