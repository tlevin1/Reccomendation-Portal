# Generated by Django 3.2 on 2021-05-02 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('more_info', '0003_auto_20210427_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moreinfo',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
