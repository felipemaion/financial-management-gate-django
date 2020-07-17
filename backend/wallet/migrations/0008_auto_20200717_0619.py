# Generated by Django 3.0.3 on 2020-07-17 06:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('instrument', '0020_auto_20200711_2043'),
        ('wallet', '0007_auto_20200515_0753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Position2',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated at')),
                ('date', models.DateField(verbose_name='date')),
                ('category', models.CharField(blank=True, max_length=255, null=True, verbose_name='category')),
                ('quantity', models.IntegerField(verbose_name='quantity')),
                ('total_quantity', models.IntegerField(verbose_name='total quantity')),
                ('transaction_value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='transaction value')),
                ('net_value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='net value')),
                ('total_value', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='total value')),
                ('instrument', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='instrument_position', to='instrument.Instrument')),
                ('wallet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wallet_position', to='wallet.Wallet')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
                'ordering': ['-date'],
            },
        ),
        migrations.DeleteModel(
            name='Position',
        ),
    ]
