# Generated by Django 3.2.8 on 2021-12-05 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_productimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='images',
            field=models.FileField(upload_to='product/images'),
        ),
    ]
