# Generated by Django 3.1.7 on 2021-03-29 02:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RequestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('requester', models.CharField(default='', max_length=200)),
                ('requester_email', models.EmailField(blank=True, max_length=200, null=True)),
                ('request_date', models.DateField(default=django.utils.timezone.now, max_length=100)),
                ('position', models.CharField(blank=True, max_length=100, null=True)),
                ('due_date', models.DateField(max_length=100)),
                ('writer_name', models.CharField(choices=[('Professor 1', 'Dixon'), ('Professor 2', 'Johnson'), ('Professor 2', 'Eric')], max_length=100)),
                ('company_name', models.CharField(default='', max_length=100)),
                ('company_website', models.URLField(blank=True, max_length=100, null=True)),
                ('company_email', models.EmailField(blank=True, max_length=100, null=True)),
                ('company_recipients', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Finish', 'Finish')], default='New', max_length=100)),
                ('cv', models.URLField(blank=True, max_length=100, null=True)),
                ('resume', models.URLField(blank=True, max_length=100, null=True)),
                ('transcript', models.URLField(blank=True, max_length=100, null=True)),
                ('additional_info', models.TextField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
