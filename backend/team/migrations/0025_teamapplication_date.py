# Generated by Django 4.2.7 on 2024-05-28 07:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("team", "0024_alter_teampositions_team"),
    ]

    operations = [
        migrations.AddField(
            model_name="teamapplication",
            name="date",
            field=models.DateField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]