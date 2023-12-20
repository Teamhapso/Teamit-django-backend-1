# Generated by Django 4.2.7 on 2023-12-20 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=30)),
                ('image', models.ImageField(upload_to='articles/')),
                ('writer', models.CharField(default='글쓴이', max_length=10)),
                ('link', models.URLField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
