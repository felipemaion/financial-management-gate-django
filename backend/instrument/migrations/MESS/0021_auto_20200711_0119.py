# Generated by Django 3.0.3 on 2020-07-11 01:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0020_auto_20200711_0111'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventoacao',
            unique_together={('instrument', 'ex_date', 'category', 'event_date')},
        ),
    ]
