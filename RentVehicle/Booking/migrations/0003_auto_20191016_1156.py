# Generated by Django 2.2.1 on 2019-10-16 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0002_auto_20191016_1152'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='bookingStatus',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='requestStatus',
        ),
    ]
