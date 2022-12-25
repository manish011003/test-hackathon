# Generated by Django 4.1.4 on 2022-12-24 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Videos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2000)),
                ('video', models.FileField(upload_to='video')),
                ('created_at', models.DateTimeField(default=datetime.datetime(2022, 12, 24, 7, 10, 28, 243704, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'verbose_name': 'video',
            },
        ),
    ]