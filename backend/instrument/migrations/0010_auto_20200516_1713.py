# Generated by Django 3.0.3 on 2020-05-16 17:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0009_auto_20200516_1709'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='History',
            new_name='PriceHistory',
        ),
    ]
