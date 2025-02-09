# Generated by Django 3.0.3 on 2020-07-03 22:11

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0010_auto_20200516_1713'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricehistory',
            options={'ordering': ['-date'], 'verbose_name': 'Price History', 'verbose_name_plural': 'Price Histories'},
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('data', django.contrib.postgres.fields.jsonb.JSONField()),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company', to='instrument.Instrument')),
            ],
            options={
                'verbose_name': 'Company',
                'verbose_name_plural': 'Companies',
                'ordering': ['instrument'],
            },
        ),
    ]
