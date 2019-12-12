from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
	path('', views.homepage, name = 'homepage'),

	path('registration/', views.registration, name = 'registration'),
	path('registration/result/', views.registration_result, name = 'registration_result'),
	path('registration/result/return/', views.page_return, name = 'page_return'),

	path('account_activation_sent/', views.account_activation_sent, name = 'account_activation_sent'), # url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-])+/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.activate, name = 'activate'),
	path('activate/<uidb64>/<token>/', views.activate, name = 'activate'),

	path('logon/', views.logon, name = 'logon'),
	path('logon/result/', views.logon_result, name = 'logon_result'),
	path('logoff/', views.logoff, name = 'logoff'),

	path('profile/', views.profile, name = 'profile'),
	path('profile/<username>/', views.user_profile, name = 'user_profile'),
	path('profile_edit/', views.profile_edit, name = 'profile_edit'),
	path('profile_edit/result/', views.profile_edit_result, name = 'profile_edit_result'),
	path('profile_edit/result/return/', views.page_return, name = 'page_return'),

	path('advanced_search/', views.advanced_search, name = 'advanced_search'),
	path('advanced_search/result/', views.advanced_search_result, name = 'advanced_search_result'),
	path('search/result/', views.search_result, name = 'search_result'),

	path('facility/list/', views.facility_list, name = 'facility_list'),
	path('facility/<int:pk>/', views.facility_detail, name = 'facility_detail'),
	
	path('sportsfield/list/', views.sportsfield_list, name = 'sportsfield_list'),
	path('sportsfield/<int:pk>/', views.sportsfield_detail, name = 'sportsfield_detail'),

	path('sportsfield/<int:pk>/comment/', views.comment, name = 'comment'),
	path('sportsfield/comment/result/', views.comment_result, name = 'comment_result'),

	path('chat/', views.chat, name = 'chat'),
	path('chat/<int:sender>/<int:receiver>', views.message_mode, name = 'messaging'),

	path('appointment/list/', views.appointment_list, name = 'appointment_list'),
	path('appointment/new/', views.appointment_new, name = 'appointment_new'),
	path('appointment/<int:pk>/', views.appointment_join, name = 'appointment_join'),
	path('appointment/join_result/<int:pk>/', views.appointment_join_result, name = 'appointment_join_result'),
]