# Generated by Django 3.2.8 on 2021-12-05 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0020_alter_profile_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]