# Generated by Django 3.2.8 on 2021-12-11 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0023_profile_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(default='0', max_length=12),
        ),
    ]
