# Generated by Django 3.0.3 on 2020-07-10 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0017_auto_20200710_1011'),
    ]

    operations = [
        migrations.AddField(
            model_name='instrument',
            name='external_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='external id'),
        ),
    ]
