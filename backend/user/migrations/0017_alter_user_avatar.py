# Generated by Django 4.2.7 on 2023-12-03 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0016_remove_user_notifications"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.CharField(blank=True, default="png"),
        ),
    ]