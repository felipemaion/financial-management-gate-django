# Generated by Django 3.0.3 on 2020-09-05 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0018_auto_20200811_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='current_value',
            field=models.DecimalField(decimal_places=2, max_digits=20, null=True, verbose_name='current value'),
        ),
    ]
