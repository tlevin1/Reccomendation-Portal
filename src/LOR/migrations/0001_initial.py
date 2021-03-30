# Generated by Django 3.1.7 on 2021-03-30 20:07

from django.db import migrations, models
import django.db.models.deletion


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
            name='LorUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('name_title', models.CharField(max_length=25)),
                ('role', models.CharField(max_length=2)),
                ('position', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='LorRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_name', models.CharField(max_length=100)),
                ('request_initial_date', models.DateField()),
                ('request_final_date', models.DateField()),
                ('requester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_requester_id', to='LOR.loruser')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_writer_id', to='LOR.loruser')),
            ],
        ),
        migrations.CreateModel(
            name='LorDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_name', models.CharField(max_length=100)),
                ('document_type', models.CharField(max_length=2)),
                ('request_document', models.TextField()),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_document_request_id', to='LOR.lorrequest')),
            ],
        ),
        migrations.CreateModel(
            name='LorCompanyRecipient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recipient_name', models.CharField(max_length=100)),
                ('company_name', models.CharField(max_length=100)),
                ('company_website', models.URLField()),
                ('company_email', models.EmailField(max_length=254)),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='related_recipient_request_id', to='LOR.lorrequest')),
            ],
        ),
    ]
