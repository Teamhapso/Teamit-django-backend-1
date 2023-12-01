# Generated by Django 4.2.7 on 2023-12-01 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0012_alter_userprofile_education_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="userprofile",
            name="certificates",
            field=models.CharField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="education",
            field=models.CharField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="experiences",
            field=models.CharField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="keywords",
            field=models.CharField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="links",
            field=models.CharField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="short_pr",
            field=models.CharField(blank=True, default="", max_length=50),
        ),
        migrations.AlterField(
            model_name="userprofile",
            name="tools",
            field=models.CharField(blank=True, default=""),
        ),
    ]
