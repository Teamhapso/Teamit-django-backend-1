# Generated by Django 4.2.7 on 2023-12-03 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0018_userprofile_friends"),
    ]

    operations = [
        migrations.AlterField(
            model_name="friendrequest",
            name="from_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sent_requests",
                to="user.userprofile",
            ),
        ),
        migrations.AlterField(
            model_name="friendrequest",
            name="to_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="received_requests",
                to="user.userprofile",
            ),
        ),
    ]