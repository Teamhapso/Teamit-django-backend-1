# Generated by Django 4.2.7 on 2023-12-30 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0029_user_blocked_teams_user_blocked_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.CharField(max_length=128, primary_key=True, serialize=False),
        ),
    ]
