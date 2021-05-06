# Generated by Django 3.2 on 2021-05-02 21:00

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('LOR', '0028_alter_req_a_a_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='lor',
            name='requester_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_lormodel_requester_id', to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Requester'),
        ),
        migrations.AddField(
            model_name='lor',
            name='writer_fk',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='related_lormodel_writer_id', to=settings.AUTH_USER_MODEL, unique=True, verbose_name='Writer'),
        ),
        migrations.AlterField(
            model_name='req_a',
            name='A_date',
            field=models.DateField(default=datetime.datetime(2021, 5, 2, 17, 0, 21, 479810)),
        ),
    ]
