# Generated by Django 3.2.12 on 2022-03-18 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0013_remove_orderdetailssupplier_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetailssupplier',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='orders.order'),
            preserve_default=False,
        ),
    ]