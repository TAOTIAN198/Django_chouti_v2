# Generated by Django 2.0.4 on 2018-05-05 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20180505_1740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='ctime',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
