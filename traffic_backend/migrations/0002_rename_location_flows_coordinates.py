# Generated by Django 4.0.6 on 2022-07-13 02:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='flows',
            old_name='location',
            new_name='coordinates',
        ),
    ]