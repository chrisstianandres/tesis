# Generated by Django 2.0.6 on 2020-03-25 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lista', '0020_auto_20200325_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listado',
            name='fecha',
            field=models.DateField(default=datetime.datetime(2020, 3, 25, 18, 35, 44, 151260)),
        ),
    ]