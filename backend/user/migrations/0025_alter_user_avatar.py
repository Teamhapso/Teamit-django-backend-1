# Generated by Django 4.2.7 on 2023-12-19 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0024_alter_user_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(default='avatars/1.png', upload_to='avatars/'),
        ),
    ]