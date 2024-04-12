# Generated by Django 4.2.7 on 2024-04-10 10:36

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("activity", "0001_initial"),
        ("user", "0035_userposition_userinterest_usercity_useractivity_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="experiences",
        ),
        migrations.AddField(
            model_name="user",
            name="created_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="useractivity",
            name="priority",
            field=models.PositiveSmallIntegerField(
                choices=[(2, "Low"), (1, "Medium"), (0, "High")], default=0
            ),
        ),
        migrations.AlterField(
            model_name="usercity",
            name="priority",
            field=models.PositiveSmallIntegerField(
                choices=[(2, "Low"), (1, "Medium"), (0, "High")], default=0
            ),
        ),
        migrations.AlterField(
            model_name="userinterest",
            name="priority",
            field=models.PositiveSmallIntegerField(
                choices=[(2, "Low"), (1, "Medium"), (0, "High")], default=0
            ),
        ),
        migrations.AlterField(
            model_name="userposition",
            name="priority",
            field=models.PositiveSmallIntegerField(
                choices=[(2, "Low"), (1, "Medium"), (0, "High")], default=0
            ),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="keywords",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
        migrations.CreateModel(
            name="UserExperience",
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
                (
                    "image",
                    models.ImageField(
                        default="users/experience_default.png", upload_to="users/"
                    ),
                ),
                ("title", models.CharField(max_length=20)),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("pinned", models.BooleanField(default=False)),
                (
                    "activity",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="activity.activity",
                    ),
                ),
                (
                    "user_profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="experiences",
                        to="user.userprofile",
                    ),
                ),
            ],
        ),
    ]