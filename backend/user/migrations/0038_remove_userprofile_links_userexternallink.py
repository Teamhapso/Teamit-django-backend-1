# Generated by Django 4.2.7 on 2024-04-17 16:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0037_alter_userexperience_end_date_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="links",
        ),
        migrations.CreateModel(
            name="UserExternalLink",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="")),
                ("url", models.URLField()),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="external_links",
                        to="user.userprofile",
                    ),
                ),
            ],
        ),
    ]
