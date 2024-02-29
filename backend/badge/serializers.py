from rest_framework import serializers

from .models import *

BADGE_TITLES = {
     'attendance': '출석 도장 찍기',
     'friendship': '사이좋게 지내자',
     'team_participance': 'Join the team!',
     'team_post': '아아 알립니다',
     'liked': '넌 내가 찜했어',
     'recruit': '너 내 동료가 돼라',
     'team_refusal': '강철 심장',
     'user_profile': '위대한 첫걸음', 
     'team_leader': '팀 리더', 
     'shared_profile': 'shared profile title'
}

BADGE_SUBTITLES = {
     'attendance': '근면 성실한 게더어스 러버',
     'friendship': '게더어스의 능력자들과 친해져 봐요!',
     'team_participance': '게더어스 팀에 참여해보세요!',
     'team_post': '팀 게시글을 작성해보세요!',
     'liked': '누군가 날 찜했어요!',
     'recruit': '능력자들과 팀을 꾸려보세요',
     'team_refusal': '실패하면 어때, 다시 해보면 되지!',
     'user_profile': '게더어스에 도착했어요', 
     'team_leader': '내가 리더가 될 상인가?', 
     'shared_profile': 'shared profile subtitle'
}
class BadeDetailSerializer(serializers.ModelSerializer):
     class Meta:
          model = Badge
          fields = [
               'user',
               'attendatnce_level', 
               'friendship_level',
               'team_participance_level',
               'team_post_level',
               'liked_level',
               'recruit_level',
               'team_refusal_status',
               'user_profile_status',
               'team_leader_status',
               'shared_profile_level'
          ]
          
     def to_representation(self, instance):
          data =  super().to_representation(instance)
          result = {}
          for field_name, value in data.items():
               if field_name == 'user':
                    result[field_name] = value
                    continue
               badge_name = field_name.split('_')[0]
               result[badge_name] = {
                    'title': BADGE_TITLES[badge_name],
                    'subtitle': BADGE_SUBTITLES[badge_name],
                    'level': value
               }
          return result