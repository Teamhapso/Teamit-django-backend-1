# Generated by Django 4.2.7 on 2024-02-20 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("chat", "0022_inquirymessage_is_msg"),
    ]

    operations = [
        migrations.AlterField(
            model_name="inquirymessage",
            name="timestamp",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
