# Generated by Django 3.2.9 on 2021-11-30 16:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20211130_1629'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
