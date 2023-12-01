# Generated by Django 4.2.7 on 2023-11-30 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("activity", "0001_initial"),
        ("user", "0008_userprofile_activity_alter_userprofile_city_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="activity",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="activities",
            field=models.ManyToManyField(related_name="users", to="activity.activity"),
        ),
    ]
