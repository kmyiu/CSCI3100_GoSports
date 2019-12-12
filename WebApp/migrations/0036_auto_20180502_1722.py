# Generated by Django 2.0.3 on 2018-05-02 09:22

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0035_auto_20180502_1401'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentonsportsfield',
            name='rate',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]