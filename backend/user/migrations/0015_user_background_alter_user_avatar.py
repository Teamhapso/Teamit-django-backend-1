# Generated by Django 4.2.7 on 2023-12-03 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0014_friendrequest"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="background",
            field=models.CharField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="user",
            name="avatar",
            field=models.CharField(blank=True, default=""),
        ),
    ]
