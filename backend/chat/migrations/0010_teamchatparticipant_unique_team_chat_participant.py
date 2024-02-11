# Generated by Django 4.2.7 on 2024-02-10 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0009_alter_teamchatroom_background"),
    ]

    operations = [
        migrations.AddConstraint(
            model_name="teamchatparticipant",
            constraint=models.UniqueConstraint(
                fields=("chatroom", "user"), name="unique_team_chat_participant"
            ),
        ),
    ]
