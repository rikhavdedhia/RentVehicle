# Generated by Django 2.2.1 on 2019-10-16 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dropdowndb', '0002_bookingstatus_requeststatus'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookingstatus',
            name='statusId',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='requeststatus',
            name='statusId',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
