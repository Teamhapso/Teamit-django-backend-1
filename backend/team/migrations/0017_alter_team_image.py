# Generated by Django 4.2.7 on 2023-12-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0016_alter_team_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='image',
            field=models.ImageField(default='teams/default.png', null=True, upload_to='teams/'),
        ),
    ]