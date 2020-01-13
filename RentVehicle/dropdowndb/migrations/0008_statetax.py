# Generated by Django 2.2.1 on 2019-10-29 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dropdowndb', '0007_remove_acceptrejectbooking_arid'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateTax',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.DecimalField(decimal_places=4, max_digits=5)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dropdowndb.State')),
            ],
        ),
    ]
