# Generated by Django 2.0.6 on 2020-03-27 19:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0025_auto_20200325_1903'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listado',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 3, 27, 19, 48, 6, 488596)),
        ),
    ]