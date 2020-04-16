# Generated by Django 3.0.3 on 2020-04-16 06:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20200416_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
    ]
