# Generated by Django 3.2.12 on 2022-02-03 04:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0003_auto_20220203_0605'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='maincategory',
            options={'verbose_name_plural': '2.MainCategory'},
        ),
        migrations.AlterModelOptions(
            name='minicategory',
            options={'verbose_name_plural': '4.MiniCategory'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name_plural': '3.SubCategory'},
        ),
        migrations.AlterModelOptions(
            name='supercategory',
            options={'verbose_name_plural': '1.SuperCategory'},
        ),
    ]
