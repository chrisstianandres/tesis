# Generated by Django 2.0.6 on 2020-03-31 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docente', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='docente',
            name='rol',
            field=models.IntegerField(choices=[(0, 'Admin'), (1, 'Docente')], default=1),
        ),
    ]