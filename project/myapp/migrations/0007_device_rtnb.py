# Generated by Django 4.2.4 on 2023-08-14 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_device_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='rtnb',
            field=models.IntegerField(default=0),
        ),
    ]