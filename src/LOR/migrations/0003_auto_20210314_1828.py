# Generated by Django 3.1.7 on 2021-03-14 18:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LOR', '0002_auto_20210313_2152'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lor',
            old_name='requester',
            new_name='requester_email',
        ),
    ]