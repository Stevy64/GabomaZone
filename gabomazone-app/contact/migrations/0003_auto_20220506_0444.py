# Generated by Django 3.1.2 on 2022-05-06 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_auto_20220506_0441'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='messageslist',
            options={'ordering': ('-id',), 'verbose_name': 'Message_List', 'verbose_name_plural': 'Messages_List'},
        ),
    ]