# Generated by Django 3.1.7 on 2021-04-04 16:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LOR', '0005_auto_20210404_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='req_a',
            name='A_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 4, 12, 3, 22, 741627)),
        ),
    ]
