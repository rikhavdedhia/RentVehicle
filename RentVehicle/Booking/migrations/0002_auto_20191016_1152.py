# Generated by Django 2.2.1 on 2019-10-16 15:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dropdowndb', '0002_bookingstatus_requeststatus'),
        ('Booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='bookingStatus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.BookingStatus'),
        ),
        migrations.AddField(
            model_name='booking',
            name='requestStatus',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.RequestStatus'),
        ),
    ]