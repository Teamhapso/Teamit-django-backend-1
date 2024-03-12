# Generated by Django 4.2.7 on 2024-03-12 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("badge", "0003_badge_review_status"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="badge",
            name="recruit_level",
        ),
        migrations.RemoveField(
            model_name="badge",
            name="team_participance_level",
        ),
        migrations.AddField(
            model_name="badge",
            name="recruit_cnt",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name="badge",
            name="team_participance_cnt",
            field=models.PositiveIntegerField(default=0),
        ),
    ]