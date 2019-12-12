from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from .models_user import CustomUser

# This defines the choices of interested sports
SPORTS_CHOICES = (
	('Badminton', 'Badminton'), 
	('Baseball', 'Baseball'), 
	('Basketball', 'Basketball'), 
	('Climbing', 'Climbing'),
	('Cycling', 'Cycling'), 
	('Dancing', 'Dancing'), 
	('Dodgeball', 'Dodgeball'), 
	('Football', 'Football'), 
	('Golf', 'Golf'), 
	('Gymnasium', 'Gymnasium'), 
	('Hiking', 'Hiking'), 
	('Pool', 'Pool'),
	('Running', 'Running'), 
	('Skipping', 'Skipping'), 
	('Snooker', 'Snooker'),
	('Softball', 'Softball'), 
	('Squash', 'Squash'),
	('Swimming', 'Swimming'), 
	('Table Tennis', 'Table Tennis'), 
	('Tennis', 'Tennis'), 
	('Volleyball', 'Volleyball'), 
	('Woodball', 'Woodball'), 
	('Others', 'Others'),
	)

# This defines the choices of the 18 districts in Hong Kong
DISTRICT_CHOICE = (
    ('Central and Western', 'Central and Western'),
    ('Wanchai', 'Wanchai'),
    ('Eastern', 'Eastern'),
    ('Southern', 'Southern'),
    ('Kowloon City', 'Kowloon City'),
    ('Wong Tai Sin', 'Wong Tai Sin'),
    ('Kwun Tong', 'Kwun Tong'),
    ('Yau Tsim Mong', 'Yau Tsim Mong'),
    ('Sham Shui Po', 'Sham Shui Po'),
    ('Tsuen Wan', 'Tsuen Wan'),
    ('Kwai Tsing', 'Kwai Tsing'),
    ('Sai Kung', 'Sai Kung'),
    ('Shatin', 'Shatin'),
    ('Tai Po', 'Tai Po'),
    ('Northern', 'Northern'),
    ('Tuen Mun', 'Tuen Mun'),
    ('Yuen Long', 'Yuen Long'),
    ('Island', 'Island'),
    )

# This is the database model of the facilities
class Facility(models.Model):
    name = models.CharField(max_length = 100, verbose_name = 'Name')
    district = models.CharField(max_length = 20, verbose_name = 'District', choices = DISTRICT_CHOICE)
    address = models.TextField(verbose_name = 'Address')
    latitude = models.FloatField(verbose_name = 'Latitude')
    longitude = models.FloatField(verbose_name = 'Longitude')
    rate_numerator = models.PositiveSmallIntegerField(default = 0, verbose_name = '')
    rate_denominator = models.PositiveSmallIntegerField(default = 0, verbose_name = '')
    rate = models.CharField(max_length = 4, verbose_name = 'Rate', default = 'N/A')
    sports_type = MultiSelectField(choices = SPORTS_CHOICES, default = '', verbose_name = 'Sports type')
    class Meta:
        verbose_name_plural = 'facilities'

    def __str__(self):
        return self.name