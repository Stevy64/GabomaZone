# Generated by Django 3.2.12 on 2022-03-02 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0051_alter_product_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='PRDSlug',
            field=models.SlugField(allow_unicode=True, blank=True, max_length=150, null=True, unique=True, verbose_name='Slugfiy'),
        ),
    ]