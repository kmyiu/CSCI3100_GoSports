# Generated by Django 2.0.1 on 2018-04-03 15:38

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0024_auto_20180403_2258'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='propic',
            field=models.ImageField(blank=True, help_text='Optional. You could upload your personal profile picture.', upload_to='', verbose_name='Picture'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='sports_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('badminton', 'Badminton'), ('baseball', 'Baseball'), ('basketball', 'Basketball'), ('climbing', 'Climbing'), ('cycling', 'Cycling'), ('dancing', 'Dancing'), ('dodgeball', 'Dodgeball'), ('football', 'Football'), ('golf', 'Golf'), ('gymnasium', 'Gymnasium'), ('hiking', 'Hiking'), ('pool', 'Pool'), ('running', 'Running'), ('skipping', 'Skipping'), ('snooker', 'Snooker'), ('softball', 'Softball'), ('squash', 'Squash'), ('swimming', 'Swimming'), ('table_tennis', 'Table Tennis'), ('tennis', 'Tennis'), ('volleyball', 'Volleyball'), ('woodball', 'Woodball'), ('others', 'Others')], default='', max_length=197, verbose_name='Sports type'),
        ),
        migrations.AlterField(
            model_name='sportsfield',
            name='sports_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('badminton', 'Badminton'), ('baseball', 'Baseball'), ('basketball', 'Basketball'), ('climbing', 'Climbing'), ('cycling', 'Cycling'), ('dancing', 'Dancing'), ('dodgeball', 'Dodgeball'), ('football', 'Football'), ('golf', 'Golf'), ('gymnasium', 'Gymnasium'), ('hiking', 'Hiking'), ('pool', 'Pool'), ('running', 'Running'), ('skipping', 'Skipping'), ('snooker', 'Snooker'), ('softball', 'Softball'), ('squash', 'Squash'), ('swimming', 'Swimming'), ('table_tennis', 'Table Tennis'), ('tennis', 'Tennis'), ('volleyball', 'Volleyball'), ('woodball', 'Woodball'), ('others', 'Others')], default='', max_length=197, verbose_name='Sports type'),
        ),
    ]
