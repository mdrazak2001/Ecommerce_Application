# Generated by Django 3.2.8 on 2021-11-29 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_product_price_in_rupees'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]
