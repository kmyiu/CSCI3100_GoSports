# Generated by Django 2.0.3 on 2018-03-16 14:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('password', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=40)),
                ('birthday', models.DateField(default=django.utils.timezone.now)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]
