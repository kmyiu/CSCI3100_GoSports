# Generated by Django 2.0.3 on 2018-05-03 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0038_auto_20180503_1731'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='starter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Starter', to=settings.AUTH_USER_MODEL),
        ),
    ]
