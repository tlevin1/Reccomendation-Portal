# Generated by Django 3.1.7 on 2021-04-04 21:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOR', '0018_auto_20210404_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='req_a',
            name='A_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 4, 17, 26, 35, 22487)),
        ),
    ]