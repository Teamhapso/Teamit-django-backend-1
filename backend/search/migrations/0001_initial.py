# Generated by Django 4.2.7 on 2024-01-03 13:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0031_user_uid_alter_user_id'),
        ('team', '0017_alter_team_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSearchHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('search_query', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('searched_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_searches', to='user.user')),
            ],
        ),
        migrations.CreateModel(
            name='TeamSearchHistory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('search_query', models.CharField(max_length=50)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('searched_team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='team.team')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='team_searches', to='user.user')),
            ],
        ),
    ]
