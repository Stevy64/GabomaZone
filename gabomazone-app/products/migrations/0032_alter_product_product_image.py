# Generated by Django 3.2.12 on 2022-03-01 00:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0031_alter_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(upload_to='products/imgs/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'png'])], verbose_name='Product Image'),
        ),
    ]
