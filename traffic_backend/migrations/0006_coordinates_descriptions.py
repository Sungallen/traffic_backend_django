# Generated by Django 4.0.6 on 2022-07-13 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic_backend', '0005_category_coordinates_alter_flows_category_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='coordinates',
            name='descriptions',
            field=models.CharField(default=12345, max_length=50),
            preserve_default=False,
        ),
    ]
