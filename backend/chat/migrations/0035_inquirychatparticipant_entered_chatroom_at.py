# Generated by Django 4.2.7 on 2024-06-22 15:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0034_privatechatparticipant_entered_chatroom_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="inquirychatparticipant",
            name="entered_chatroom_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]