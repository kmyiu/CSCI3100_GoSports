from django.db import models
from datetime import datetime
from .models import *

class Appointment(models.Model):
	starter = models.ForeignKey(User, related_name = 'Starter', on_delete = models.CASCADE)
	appointment_time = models.DateTimeField(default = datetime.now, verbose_name = 'appointment time')
	sports_type = models.CharField(max_length = 25, choices = SPORTS_CHOICES, default = '', verbose_name = 'Sports')
	location = models.CharField(max_length = 100)
	max_num = models.PositiveIntegerField(default = 1)
	joined = models.IntegerField(default = 0)
	status = models.CharField(max_length = 1, choices = (('O','open'),('F','full'),('E','ended')), default = 'O')
	remark = models.TextField(blank = True)
	participants = models.CharField(max_length=100000, default = '[]')