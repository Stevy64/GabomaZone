# Generated by Django 3.2.14 on 2022-08-14 02:36

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0064_auto_20220814_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='digital_file',
            field=models.FileField(blank=True, help_text='Please use our recommended allowed extension are zip , rar', null=True, upload_to='products/files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['zip', 'rar'])], verbose_name='Digital File'),
        ),
    ]
