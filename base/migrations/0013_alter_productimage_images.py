# Generated by Django 3.2.8 on 2021-12-05 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_alter_productimage_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productimage',
            name='images',
            field=models.ImageField(upload_to='product/images'),
        ),
    ]
