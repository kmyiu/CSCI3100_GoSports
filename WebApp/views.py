'''
This file places all functions regarding actions of webpage, it is 
divided into subfiles, please refer to the subfiles listed below. 
'''

from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from .views_authenticate import *
from .views_register import *
from .views_search import *
from .views_profile import *
from .views_facility import *
from .views_sportsfield import *
from .views_appointment import *
from .views_chat import *

def homepage(request):
	return render(request, 'WebApp/homepage.html')

def page_return(request):
	return HttpResponse('<script>history.go(-2);</script>')