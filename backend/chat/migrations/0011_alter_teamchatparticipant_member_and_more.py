# Generated by Django 4.2.7 on 2024-02-10 19:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("team", "0019_teampermission"),
        ("chat", "0010_teamchatparticipant_unique_team_chat_participant"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teamchatparticipant",
            name="member",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="participants",
                to="team.teammembers",
            ),
        ),
        migrations.AlterField(
            model_name="teamchatroom",
            name="last_msg",
            field=models.CharField(default="", max_length=255),
        ),
    ]