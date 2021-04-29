# Generated by Django 3.1.7 on 2021-04-29 20:47

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LOR', '0028_merge_20210429_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='req_a',
            name='A_date',
            field=models.DateField(default=datetime.datetime(2021, 4, 29, 16, 47, 9, 858692)),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='requester_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_requestmodel_requester_id', to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Requester'),
        ),
        migrations.AlterField(
            model_name='requestmodel',
            name='writer_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_requestmodel_writer_id', to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Writer'),
        ),
    ]
