from django.db import models
from datetime import datetime
from multiselectfield import MultiSelectField
from .models_user import CustomUser
from .models_facility import Facility
from django.core.validators import MinValueValidator, MaxValueValidator

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

# This is the database model of the sports fields
# The "rate" field stores the calculated rate, while "rate_numerator"
# and "rate_denominator" stores the preprocessed data
class SportsField(models.Model):
    name = models.CharField(max_length = 80, verbose_name = 'Name')
    opening_hour = models.TextField(verbose_name = 'Opening hour')
    can_be_booked = models.BooleanField(verbose_name = 'Can be booked')
    need_membership = models.BooleanField(verbose_name = 'Membership')
    is_free = models.BooleanField(verbose_name = 'Is free')
    payment_detail = models.TextField(verbose_name = 'Charge')
    is_indoor = models.BooleanField(verbose_name = 'Is indoor')
    rate_numerator = models.PositiveSmallIntegerField(default = 0, verbose_name = '')
    rate_denominator = models.PositiveSmallIntegerField(default = 0, verbose_name = '')
    rate = models.CharField(max_length = 4, verbose_name = 'Rate', default = 'N/A')
    sports_type = MultiSelectField(choices = SPORTS_CHOICES, default = '', verbose_name = 'Sports type')
    remark = models.TextField(verbose_name = 'Remark', blank = True)
    belongs_to = models.ForeignKey(Facility, related_name ='belong_to', on_delete = models.CASCADE, default = None)

    def __str__(self):
        return self.name

# This is the database model of the comment on sportsfields
class CommentOnSportsField(models.Model):
    commenter = models.ForeignKey(CustomUser, related_name = 'SportsFieldCommenter', on_delete = models.CASCADE)
    target_sportsfield = models.ForeignKey(SportsField, related_name = 'CommentTargetedSportsField', on_delete = models.CASCADE)
    comment = models.TextField(blank = True)
    rate = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    timestamp = models.DateTimeField(default = datetime.now)
    class Meta:
        ordering = ('timestamp', )

    def __str__(self):
        return self.commenter.username + " comment's on " + self.target_sportsfield.name