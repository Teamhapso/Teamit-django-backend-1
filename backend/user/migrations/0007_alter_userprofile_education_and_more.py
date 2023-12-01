# Generated by Django 4.2.7 on 2023-11-25 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0006_alter_userprofile_certificates_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="education",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="experiences",
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="links",
            field=models.JSONField(default=dict),
        ),
    ]
