from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from GoSports.settings import MESSAGE_MANAGER_RECEIVER, MESSAGE_MANAGER_SENDER
from datetime import datetime
from .models import *

# This view handles the chatroom function
def chat(request):
	if not request.user.is_authenticated:
		return redirect('homepage')
	if request.method == 'GET':
		MESSAGE_MANAGER_SENDER = -1
		MESSAGE_MANAGER_RECEIVER = -1
		return render(request, 'WebApp/chat.html', {'users': CustomUser.objects.exclude(username = request.user.username),
			'enabled': False})

# This view handles the messaging function
def message_mode(request, sender, receiver):
	global MESSAGE_MANAGER_SENDER, MESSAGE_MANAGER_RECEIVER
	if not request.user.is_authenticated:
		return redirect('homepage')
	if request.method == 'GET':
		MESSAGE_MANAGER_SENDER = sender
		MESSAGE_MANAGER_RECEIVER = receiver
		user_sender , user_receiver = CustomUser.objects.get(id = sender), CustomUser.objects.get(id = receiver)
		w = Message.objects.filter(Q(sender_id = user_sender, receiver_id = user_receiver) |
								Q(sender_id = user_receiver, receiver_id = user_sender))
		return render(request, 'WebApp/chat.html',
					{'users': CustomUser.objects.exclude(username = request.user.username), 
					'receiver': user_receiver,   
					'sender': user_sender, 
					'messages': Message.objects.filter(Q(sender_id = user_sender, receiver_id = user_receiver) |
								Q(sender_id = user_receiver, receiver_id = user_sender)),
					'enabled': True})	
	if request.method == 'POST':
		if request.POST['message']:
			text = request.POST['message']
			m = Message.objects.create(message = text, receiver = CustomUser.objects.get(id = receiver),   
					sender = CustomUser.objects.get(id = sender))
		user_sender = CustomUser.objects.get(id = MESSAGE_MANAGER_SENDER)
		user_receiver = CustomUser.objects.get(id = MESSAGE_MANAGER_RECEIVER)
		return render(request, 'WebApp/chat.html',
					{'users': CustomUser.objects.exclude(username=request.user.username), 
					'receiver': user_receiver,   
					'sender': user_sender, 
					'messages': Message.objects.filter(Q(sender_id = user_sender, receiver_id = user_receiver) |
								Q(sender_id = user_receiver, receiver_id = user_sender)),
					'enabled': True})