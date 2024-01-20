# Generated by Django 4.2.7 on 2024-01-20 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notification', '0006_alter_notification_options_and_more'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='notification',
            index=models.Index(fields=['related_id', 'type'], name='related_id_type_idx'),
        ),
        migrations.AddIndex(
            model_name='teamnotification',
            index=models.Index(fields=['type'], name='type_idx'),
        ),
    ]