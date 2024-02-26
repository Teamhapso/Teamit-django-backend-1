# Generated by Django 4.2.7 on 2024-02-13 14:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("team", "0019_teampermission"),
        ("chat", "0013_inquirychatroom_inquirer_alarm_on_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inquirychatroom",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="inquiry_chat_rooms",
                to="team.team",
            ),
        ),
        migrations.AlterField(
            model_name="teamchatparticipant",
            name="is_online",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="teammessage",
            name="chatroom",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="messages",
                to="chat.teamchatroom",
            ),
        ),
        migrations.AlterField(
            model_name="teammessage",
            name="sender",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="chat.teamchatparticipant",
            ),
        ),
        migrations.AlterField(
            model_name="teammessage",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
