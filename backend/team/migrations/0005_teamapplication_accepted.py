# Generated by Django 4.2.7 on 2023-12-03 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("team", "0004_remove_teammembers_avatar_team_creator_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="teamapplication",
            name="accepted",
            field=models.BooleanField(default=False),
        ),
    ]
