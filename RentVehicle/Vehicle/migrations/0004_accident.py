# Generated by Django 2.2.1 on 2019-11-11 01:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Vehicle', '0003_auto_20191015_1041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disabled', models.BooleanField()),
                ('description', models.CharField(max_length=512)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Vehicle.Vehicle')),
            ],
        ),
    ]
