# Generated by Django 2.0.1 on 2018-03-17 09:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('WebApp', '0002_facilitie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blacklist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('district', models.CharField(max_length=25)),
                ('address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='FriendList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='SportsField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('is_indoor', models.BooleanField()),
                ('can_be_booked', models.BooleanField()),
                ('working_day_booking_fare_adult', models.FloatField(default=0)),
                ('working_day_booking_fare_student', models.FloatField(default=0)),
                ('working_day_booking_fare_children', models.FloatField(default=0)),
                ('working_day_booking_fare_disabled', models.FloatField(default=0)),
                ('working_day_booking_fare_senior', models.FloatField(default=0)),
                ('holiday_booking_fare_adult', models.FloatField(default=0)),
                ('holiday_booking_fare_student', models.FloatField(default=0)),
                ('holiday_booking_fare_children', models.FloatField(default=0)),
                ('holiday_booking_fare_disabled', models.FloatField(default=0)),
                ('holiday_booking_fare_senior', models.FloatField(default=0)),
                ('remaark', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Facilitie',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='organization',
            name='founder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Founder', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendlist',
            name='friend',
            field=models.ManyToManyField(related_name='Friend', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='friendlist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FriendList_Owner', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='facility',
            name='sportsfield_included',
            field=models.ManyToManyField(to='WebApp.SportsField'),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='blocked_user',
            field=models.ManyToManyField(related_name='Blocked_User', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='blacklist',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Blacklist_Owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
