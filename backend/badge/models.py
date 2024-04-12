from django.db import models

from user.models import User

class BadgeLevels(models.IntegerChoices):
     LEVEL_DEFAULT = 0, 'Level default'
     LEVEL_ONE = 1, 'Level 1'
     LEVEL_TWO = 2, 'Level 2'
     LEVEL_THREE = 3, 'Level 3'

class BadgeType(models.IntegerChoices):
     ATTENDANCE = 0, 'Attendance'
     FRIENDSHIP = 1, 'Frienship'
     TEAM_PARTICIPANCE = 2, 'Team Participance'
     TEAM_POST = 3, 'Team Post'
     LIKED = 4, 'Liked'
     RECRUIT = 5, 'Recruit'
     TEAM_REFUSAL = 6, 'Team Refusal'
     USER_PROFILE = 7, 'User p'
     TEAM_LEADER = 8, 'Level 3'
     SHARED_PROFILE = 9, 'Level 3'
     REVIEW = 10, 'Level 3'

class Badge(models.Model):
     user = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE, related_name='badge')
     attendance_cnt = models.PositiveIntegerField(default=0)
     attendance_change = models.BooleanField(default=False)
     friendship_level = models.IntegerField(choices=BadgeLevels.choices, default=BadgeLevels.LEVEL_DEFAULT)
     friendship_change = models.BooleanField(default=False)
     team_participance_cnt = models.PositiveIntegerField(default=0)
     team_participance_change = models.BooleanField(default=False)
     team_post_level = models.IntegerField(choices=BadgeLevels.choices, default=BadgeLevels.LEVEL_DEFAULT)
     team_post_change = models.BooleanField(default=False)
     liked_level = models.IntegerField(choices=BadgeLevels.choices, default=BadgeLevels.LEVEL_DEFAULT)
     liked_change = models.BooleanField(default=False)
     recruit_cnt = models.PositiveIntegerField(default=0)
     recruit_change = models.BooleanField(default=False)
     team_refusal_status = models.BooleanField(default=False)
     team_refusal_change = models.BooleanField(default=False)
     user_profile_status = models.BooleanField(default=False)
     user_profile_change = models.BooleanField(default=False)
     team_leader_status =  models.BooleanField(default=False)
     team_leader_change = models.BooleanField(default=False)
     shared_profile_status = models.BooleanField(default=False)
     shared_profile_change = models.BooleanField(default=False)
     review_status = models.BooleanField(default=False)
     review_change = models.BooleanField(default=False)
     
     @property
     def recruit_level(self):
          if self.attendance_cnt >= 30:
               return BadgeLevels.LEVEL_THREE
          elif self.attendance_cnt >= 15:
               return BadgeLevels.LEVEL_TWO
          elif self.attendance_cnt >= 5:
               return BadgeLevels.LEVEL_ONE
          else:
               return BadgeLevels.LEVEL_DEFAULT
     
     @property
     def team_participance_level(self):
          if self.attendance_cnt >= 5:
               return BadgeLevels.LEVEL_THREE
          elif self.attendance_cnt >= 3:
               return BadgeLevels.LEVEL_TWO
          elif self.attendance_cnt >= 1:
               return BadgeLevels.LEVEL_ONE
          else:
               return BadgeLevels.LEVEL_DEFAULT
     
     @property
     def attendance_level(self):
          if self.attendance_cnt >= 25:
               return BadgeLevels.LEVEL_THREE
          elif self.attendance_cnt >= 14:
               return BadgeLevels.LEVEL_TWO
          elif self.attendance_cnt >= 5:
               return BadgeLevels.LEVEL_ONE
          else:
               return BadgeLevels.LEVEL_DEFAULT

     @property
     def shared_profile_level(self):
          if self.shared_profile_cnt >= 30:
               return BadgeLevels.LEVEL_THREE
          elif self.shared_profile_cnt >= 20:
               return BadgeLevels.LEVEL_TWO
          elif self.shared_profile_cnt >= 10:
               return BadgeLevels.LEVEL_ONE
          else:
               return BadgeLevels.LEVEL_DEFAULT
          