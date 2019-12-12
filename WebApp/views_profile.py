from django.db.models import Field
from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProfileEditForm
from .models import CustomUser, User

fields_base_name =  ['propic', 'username', 'first_name', 'last_name', 'nickname', 'gender', 'interest', 'self_introduction', ]
profile_header = ['first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'interest', 'self_introduction', 'propic']

# This view handles the profile page
def profile(request):
	if request.method == "POST":
		username = request.POST['username']
	else:
		username = request.user.username
	if username == 'gosports_admin':
		user_base = User.objects.get(username = username)
		fields = [field for field in User._meta.get_fields() if field.name in fields_base_name]
	else:
		user_base = get_object_or_404(CustomUser, username = username)
		fields = [field for field in CustomUser._meta.get_fields() if field.name in fields_base_name]
	user = {}
	if user_base:
		for field in fields:
			if field.name == 'propic':
				user[field.verbose_name] = user_base.propic.url
			else:
				user[field.verbose_name] = user_base.__getattribute__(field.name)
	return render(request, 'WebApp/profile.html', {'user': user})

# This view handles the profile page
def user_profile(request, username):
	if username == 'gosports_admin':
		user_base = User.objects.get(username = username)
		fields = [field for field in User._meta.get_fields() if field.name in fields_base_name]
	else:
		user_base = get_object_or_404(CustomUser, username = username)
		fields = [field for field in CustomUser._meta.get_fields() if field.name in fields_base_name]
	user = {}
	if user_base:
		for field in fields:
			if field.name == 'propic':
				user[field.verbose_name] = user_base.propic.url
			else:
				user[field.verbose_name] = user_base.__getattribute__(field.name)
	return render(request, 'WebApp/profile.html', {'user': user})

# This view handles editing profile
def profile_edit(request):
	if request.method == "POST":
		form = ProfileEditForm(request.POST, request.FILES)
		errors = []
		if form.is_valid():
			user = form.save()
			user.pk = request.user.pk
			user.save(update_fields=profile_header)
		else:
			for error_key in form.errors.keys():
				errors.append(form.errors[error_key])
		request.session['errors'] = errors
		return redirect('profile_edit_result')
	else:
		user = CustomUser.objects.get(username = request.user.username)
		form = ProfileEditForm(instance = user)
	return render(request, 'WebApp/profile_edit.html', {'form': form})

def profile_edit_result(request):
		return render(request, 'WebApp/profile_edit_result.html', {'errors': request.session.get('errors')})