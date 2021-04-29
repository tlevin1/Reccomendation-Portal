# Generated by Django 3.1.7 on 2021-04-27 19:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('more_info', '0002_auto_20210427_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='moreinfo',
            name='send_to',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='moreinfo',
            name='date',
            field=models.DateField(default=datetime.datetime(2021, 4, 27, 19, 54, 14, 570943, tzinfo=utc)),
        ),
    ]