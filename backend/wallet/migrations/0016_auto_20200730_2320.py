# Generated by Django 3.0.3 on 2020-07-30 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0015_auto_20200730_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='quantity',
            field=models.DecimalField(decimal_places=9, max_digits=20, null=True, verbose_name='quantity'),
        ),
    ]
