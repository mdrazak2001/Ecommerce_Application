# Generated by Django 3.2.8 on 2021-12-11 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sellerView', '0002_order_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='time',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2021, 12, 11, 19, 56, 17, 560261)),
        ),
    ]
