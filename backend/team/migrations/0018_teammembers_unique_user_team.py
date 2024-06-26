# Generated by Django 4.2.7 on 2024-01-20 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0017_alter_team_image'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='teammembers',
            constraint=models.UniqueConstraint(fields=('user', 'team'), name='unique_user_team'),
        ),
    ]
