# Generated by Django 2.2.1 on 2019-10-23 02:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dropdowndb', '0007_remove_acceptrejectbooking_arid'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcceptRejectBooking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.AcceptRejectBooking')),
            ],
        ),
    ]