# Generated by Django 2.0.3 on 2018-04-03 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0016_auto_20180403_1413'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='address',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='included_sportsfield',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='is_indoor',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='location',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='opening_hour',
        ),
        migrations.RemoveField(
            model_name='sportsfield',
            name='district',
        ),
        migrations.RemoveField(
            model_name='sportsfield',
            name='location',
        ),
        migrations.AddField(
            model_name='facility',
            name='lat',
            field=models.FloatField(default=0, verbose_name='Latitude'),
        ),
        migrations.AddField(
            model_name='facility',
            name='lng',
            field=models.FloatField(default=0, verbose_name='Longitude'),
        ),
        migrations.AddField(
            model_name='sportsfield',
            name='belongs_to',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='belong_to', to='WebApp.Facility'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='district',
            field=models.CharField(choices=[('CAW', 'Central and Western District'), ('WC', 'Wanchai District'), ('E', 'Eastern District'), ('S', 'Southern District'), ('KNC', 'Kowloon City District'), ('WTS', 'Wong Tai Sin District'), ('KT', 'Kwun Tong District'), ('YTW', 'Yau Tsim Mong District'), ('SSP', 'Sham Shui Po District'), ('TW', 'Tsuen Wan District'), ('KT', 'Kwai Tsing District'), ('SK', 'Sai Kung District'), ('ST', 'Shatin District'), ('TP', 'Tai Po District'), ('N', 'Northern District'), ('TM', 'Tuen Mun District'), ('YL', 'Yuen Long District'), ('I', 'Island District')], max_length=3, verbose_name='District'),
        ),
    ]
