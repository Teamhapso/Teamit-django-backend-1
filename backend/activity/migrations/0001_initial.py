# Generated by Django 4.2.7 on 2023-11-25 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activity",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=10, unique=True)),
                ("total_cnt", models.IntegerField(default=0)),
            ],
        ),
    ]
