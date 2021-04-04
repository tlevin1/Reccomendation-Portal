# Generated by Django 3.1.7 on 2021-04-04 15:46

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LOR',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester', models.CharField(max_length=100)),
                ('requester_email', models.EmailField(max_length=100)),
                ('request_date', models.DateField()),
                ('position', models.CharField(max_length=100)),
                ('due_date', models.DateField()),
                ('writer_email', models.EmailField(max_length=254)),
                ('company_name', models.CharField(max_length=100)),
                ('company_website', models.URLField()),
                ('company_email', models.EmailField(max_length=254)),
                ('company_recipients', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=20)),
                ('cv', models.TextField()),
                ('resume', models.TextField()),
                ('transcript', models.TextField()),
                ('additional_info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Req_a',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('answer', models.CharField(blank=True, max_length=100)),
                ('R_date', models.DateField(blank=True)),
                ('A_date', models.DateField(default=datetime.datetime(2021, 4, 4, 11, 46, 18, 464572))),
            ],
        ),
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester', models.CharField(default='', max_length=100)),
                ('requester_email', models.EmailField(blank=True, max_length=200, null=True)),
                ('request_date', models.DateField(default=django.utils.timezone.now, max_length=100)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('due_date', models.DateField(max_length=100)),
                ('writer_name', models.CharField(choices=[('Professor 1', 'Dixon'), ('Professor 2', 'Johnson'), ('Professor 2', 'Eric')], max_length=100)),
                ('writer_email', models.EmailField(blank=True, max_length=200, null=True)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('company_website', models.URLField(blank=True, max_length=100, null=True)),
                ('company_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('company_recipients', models.CharField(blank=True, max_length=200, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Finish', 'Finish')], default='New', max_length=20)),
                ('cv', models.URLField(blank=True, max_length=100, null=True)),
                ('resume', models.URLField(blank=True, max_length=100, null=True)),
                ('transcript', models.URLField(blank=True, max_length=100, null=True)),
                ('additional_info', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
