# Generated by Django 2.2.1 on 2019-11-10 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0011_auto_20191030_1135'),
        ('Renter', '0002_vehiclefeedback_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehiclefeedback',
            name='booking',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Booking.Booking'),
        ),
    ]
