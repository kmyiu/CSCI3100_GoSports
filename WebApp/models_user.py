from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from multiselectfield import MultiSelectField

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

# This is the database model of the users, which override the build-in class "User"
class CustomUser(User):
    propic = models.ImageField(blank = True, help_text = 'Optional. You could upload your personal profile picture.', verbose_name = 'Propic', default = 'default_propic.png')
    gender = models.CharField(max_length = 6, choices = (('Male', 'Male'), ('Female', 'Female')), help_text = 'Required. Choose according to your gender.', verbose_name = 'Gender')
    date_of_birth = models.DateField(help_text = 'Required. Input your date of birth.', verbose_name = 'Date of birth')
    is_email_confirmed = models.BooleanField(default = False, verbose_name = '')
    setattr(User._meta.get_field('email'), 'verbose_name', 'Email')
    setattr(User._meta.get_field('username'), 'verbose_name', 'Username')
    setattr(User._meta.get_field('first_name'), 'help_text', 'Optional. 30 characters or fewer.')
    setattr(User._meta.get_field('first_name'), 'verbose_name', 'First name')
    setattr(User._meta.get_field('last_name'), 'help_text', 'Optional. 150 characters or fewer.')
    setattr(User._meta.get_field('last_name'), 'verbose_name', 'Last name')
    setattr(User._meta.get_field('groups'), 'verbose_name', 'Group')
    nickname = models.CharField(max_length = 150, help_text = 'Required. Please enter your nickname.', unique = True, verbose_name = 'Nickname')
    interest = MultiSelectField(choices = SPORTS_CHOICES, default = '', help_text = 'Optional. Please select the sports that you are interested.', verbose_name = 'Interest', blank = True)
    self_introduction = models.TextField(blank = True, help_text = 'Optional. You could introduce yourself here.', verbose_name = 'Self introduction')

# This is the database model of the chat messages
class Message(models.Model):
    sender = models.ForeignKey(CustomUser, related_name = 'MessageSender', on_delete = models.CASCADE)
    receiver = models.ForeignKey(CustomUser, related_name = 'MessageReceiver', on_delete = models.CASCADE)
    message = models.TextField(help_text = 'Please type your message here.')
    timestamp = models.DateTimeField(default = datetime.now)
    class Meta:
        ordering = ('timestamp', )