from django.contrib.auth import login, logout
from django.shortcuts import render, redirect
from .forms import AuthenticationForm

# This view handles the log-in function
def logon(request):
	if request.method == "POST":
		form = AuthenticationForm(request, request.POST)
		errors = []
		if form.is_valid():
			login(request, form.get_user())
		else:
			for error_key in form.errors.keys():
				errors.append(form.errors[error_key])
			request.session['errors'] = errors
		return redirect('logon_result')
	else:
		form = AuthenticationForm()
		return render(request, 'WebApp/logon.html', {'form': form})

# This view handles the log-in results
def logon_result(request):
	return render(request, 'WebApp/logon_result.html', {'errors': request.session.get('errors')})

# This view handles the log-out function
def logoff(request):
	username = request.user.get_username()
	logout(request)
	return render(request, 'WebApp/logoff_result.html', {'username': username})