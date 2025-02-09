# Generated by Django 3.0.3 on 2020-07-11 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0019_auto_20200711_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='split',
            name='fraction_date',
            field=models.DateField(blank=True, null=True, verbose_name='fraction date'),
        ),
        migrations.AlterUniqueTogether(
            name='split',
            unique_together={('instrument', 'ex_date', 'category', 'event_date', 'factor', 'income_tax_price', 'fraction_date', 'fraction_price', 'details')},
        ),
    ]
