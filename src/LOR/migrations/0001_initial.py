# Generated by Django 3.1.7 on 2021-03-30 23:24

from django.db import migrations, models


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
    ]
