# Generated by Django 2.0.1 on 2018-04-13 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0031_auto_20180412_1858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facility',
            name='remark',
        ),
    ]
