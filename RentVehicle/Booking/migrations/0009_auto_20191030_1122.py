# Generated by Django 2.2.1 on 2019-10-30 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Booking', '0008_paymentdetailscheck'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='negotiationPrice',
            field=models.DecimalField(decimal_places=2, default=False, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='negotiationRequest',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
    ]
