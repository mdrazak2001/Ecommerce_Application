# Generated by Django 3.2.8 on 2021-11-29 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_auto_20211129_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price_in_rupees',
            field=models.IntegerField(default=0),
        ),
    ]
