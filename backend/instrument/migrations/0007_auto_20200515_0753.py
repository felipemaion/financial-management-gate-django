# Generated by Django 3.0.3 on 2020-05-15 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0006_auto_20200515_0753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='PriceHistory',
            name='date',
            field=models.DateTimeField(verbose_name='date'),
        ),
    ]
