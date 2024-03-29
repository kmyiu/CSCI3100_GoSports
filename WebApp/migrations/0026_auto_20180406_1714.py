# Generated by Django 2.0.1 on 2018-04-06 09:14

import datetime
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('WebApp', '0025_auto_20180403_2338'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentOnFacility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('rate', models.PositiveSmallIntegerField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.CreateModel(
            name='CommentOnSportsField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True)),
                ('rate', models.PositiveSmallIntegerField()),
                ('timestamp', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'ordering': ('timestamp',),
            },
        ),
        migrations.RemoveField(
            model_name='commentonfacilities',
            name='commenter',
        ),
        migrations.RemoveField(
            model_name='commentonfacilities',
            name='facility',
        ),
        migrations.AlterModelOptions(
            name='blacklist',
            options={'ordering': ('friend__nickname',)},
        ),
        migrations.AlterModelOptions(
            name='friendlist',
            options={'ordering': ('friend__nickname',)},
        ),
        migrations.RenameField(
            model_name='opinion',
            old_name='target',
            new_name='target_facility',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='lat',
        ),
        migrations.RemoveField(
            model_name='facility',
            name='lng',
        ),
        migrations.AddField(
            model_name='facility',
            name='latitude',
            field=models.FloatField(default=0, verbose_name='Latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='facility',
            name='longitude',
            field=models.FloatField(default=0, verbose_name='Longitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='opinion',
            name='target_sportsfield',
            field=models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='WebApp.SportsField'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], help_text='Required. Choose according to your gender.', max_length=6, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='interest',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Badminton', 'Badminton'), ('Baseball', 'Baseball'), ('Basketball', 'Basketball'), ('Climbing', 'Climbing'), ('Cycling', 'Cyling'), ('Dancing', 'Dancing'), ('Dodgeball', 'Dodgeball'), ('Football', 'Football'), ('Golf', 'Golf'), ('Gymnasium', 'Gymnasium'), ('Hiking', 'Hiking'), ('Pool', 'Pool'), ('Running', 'Running'), ('Skipping', 'Skipping'), ('Snooker', 'Snooker'), ('Softball', 'Softball'), ('Squash', 'Squash'), ('Swimming', 'Swimming'), ('Table Tennis', 'Table Tennis'), ('Tennis', 'Tennis'), ('Volleyball', 'Volleyball'), ('Woodball', 'Woodball'), ('Others', 'Others')], default='', help_text='Optional. Please select the sports that you are interested.', max_length=197, verbose_name='Interest'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='propic',
            field=models.ImageField(blank=True, default='default_propic.png', help_text='Optional. You could upload your personal profile picture.', upload_to='', verbose_name='Propic'),
        ),
        migrations.AlterField(
            model_name='facility',
            name='sports_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Badminton', 'Badminton'), ('Baseball', 'Baseball'), ('Basketball', 'Basketball'), ('Climbing', 'Climbing'), ('Cycling', 'Cycling'), ('Dancing', 'Dancing'), ('Dodgeball', 'Dodgeball'), ('Football', 'Football'), ('Golf', 'Golf'), ('Gymnasium', 'Gymnasium'), ('Hiking', 'Hiking'), ('Pool', 'Pool'), ('Running', 'Running'), ('Skipping', 'Skipping'), ('Snooker', 'Snooker'), ('Softball', 'Softball'), ('Squash', 'Squash'), ('Swimming', 'Swimming'), ('Table Tennis', 'Table Tennis'), ('Tennis', 'Tennis'), ('Volleyball', 'Volleyball'), ('Woodball', 'Woodball'), ('Others', 'Others')], default='', max_length=197, verbose_name='Sports type'),
        ),
        migrations.AlterField(
            model_name='message',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MessageReceiver', to='WebApp.CustomUser'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='MessageSender', to='WebApp.CustomUser'),
        ),
        migrations.AlterField(
            model_name='sportsfield',
            name='sports_type',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Badminton', 'Badminton'), ('Baseball', 'Baseball'), ('Basketball', 'Basketball'), ('Climbing', 'Climbing'), ('Cycling', 'Cycling'), ('Dancing', 'Dancing'), ('Dodgeball', 'Dodgeball'), ('Football', 'Football'), ('Golf', 'Golf'), ('Gymnasium', 'Gymnasium'), ('Hiking', 'Hiking'), ('Pool', 'Pool'), ('Running', 'Running'), ('Skipping', 'Skipping'), ('Snooker', 'Snooker'), ('Softball', 'Softball'), ('Squash', 'Squash'), ('Swimming', 'Swimming'), ('Table Tennis', 'Table Tennis'), ('Tennis', 'Tennis'), ('Volleyball', 'Volleyball'), ('Woodball', 'Woodball'), ('Others', 'Others')], default='', max_length=197, verbose_name='Sports type'),
        ),
        migrations.DeleteModel(
            name='CommentOnFacilities',
        ),
        migrations.AddField(
            model_name='commentonsportsfield',
            name='commenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SportsFieldCommenter', to='WebApp.CustomUser'),
        ),
        migrations.AddField(
            model_name='commentonsportsfield',
            name='sportsfield',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='SportsField', to='WebApp.SportsField'),
        ),
        migrations.AddField(
            model_name='commentonfacility',
            name='commenter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='FacilityCommenter', to='WebApp.CustomUser'),
        ),
        migrations.AddField(
            model_name='commentonfacility',
            name='facility',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Facility', to='WebApp.Facility'),
        ),
    ]
