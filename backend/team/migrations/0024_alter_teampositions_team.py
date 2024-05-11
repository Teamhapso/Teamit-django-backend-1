# Generated by Django 4.2.7 on 2024-05-06 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("team", "0023_alter_teammembers_custom_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="teampositions",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="recruiting",
                to="team.team",
            ),
        ),
    ]