# Generated by Django 4.2.7 on 2024-04-14 09:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0037_alter_userexperience_end_date_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="userinterest",
            options={"ordering": ["priority"]},
        ),
        migrations.AlterModelOptions(
            name="userposition",
            options={"ordering": ["priority"]},
        ),
    ]