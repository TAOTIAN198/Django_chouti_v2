# Generated by Django 2.0.4 on 2018-05-05 09:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='ctime',
            field=models.TimeField(default=datetime.datetime(2018, 5, 5, 17, 40, 30, 767628)),
        ),
    ]
