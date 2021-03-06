# Generated by Django 2.2.1 on 2019-10-04 07:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dropdowndb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('insurance', models.BooleanField()),
                ('description', models.TextField()),
                ('TermsAndConditions', models.CharField(max_length=256)),
                ('VehicleRegistrationNumber', models.CharField(max_length=15, unique=True)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('securityDeposit', models.DecimalField(decimal_places=2, max_digits=6)),
                ('EZpass', models.BooleanField()),
                ('image', models.ImageField(blank=True, upload_to='car_images')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.Color')),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.Make')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.MakeModel')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.Style')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zipcode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.ZipCode')),
            ],
            options={
                'ordering': ['rating'],
            },
        ),
        migrations.CreateModel(
            name='Filter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('zipcode', models.CharField(max_length=5)),
                ('StartPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('EndPrice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.Color')),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.Make')),
                ('rating', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.Rating')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.Style')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
