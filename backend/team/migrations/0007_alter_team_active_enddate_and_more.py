# Generated by Django 4.2.7 on 2023-12-05 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("team", "0006_alter_teamapplication_accepted"),
    ]

    operations = [
        migrations.AlterField(
            model_name="team",
            name="active_enddate",
            field=models.CharField(default="1900-01-02", max_length=10),
        ),
        migrations.AlterField(
            model_name="team",
            name="active_startdate",
            field=models.CharField(default="1900-01-01", max_length=10),
        ),
        migrations.AlterField(
            model_name="team",
            name="recruit_enddate",
            field=models.CharField(default="1900-01-01", max_length=10),
        ),
        migrations.AlterField(
            model_name="team",
            name="recruit_startdate",
            field=models.CharField(default="1900-01-01", max_length=10),
        ),
    ]