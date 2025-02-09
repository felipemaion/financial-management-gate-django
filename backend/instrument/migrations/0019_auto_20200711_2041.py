# Generated by Django 3.0.3 on 2020-07-11 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0018_auto_20200711_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='split',
            name='details',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='details'),
        ),
        migrations.AlterUniqueTogether(
            name='split',
            unique_together={('instrument', 'ex_date', 'category', 'event_date', 'factor', 'income_tax_price', 'fraction_price', 'details')},
        ),
        migrations.RemoveField(
            model_name='split',
            name='fraction_date',
        ),
    ]
