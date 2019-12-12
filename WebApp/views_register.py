from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .forms import RegistrationForm
from .models import CustomUser
from .tokens import account_activation_token

# This view handles the registration
def registration(request):
	if request.method == "POST":
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = form.save()
			user.is_active = False
			user.save()
			# login(request, user)
			current_site = get_current_site(request)
			subject = 'Activate Your GoSports Account'
			message = render_to_string('WebApp/account_activation_email.html',{'user': user, 'domain': current_site.domain, 'uid': force_text(urlsafe_base64_encode(force_bytes(user.pk))), 'token': account_activation_token.make_token(user), })
			user.email_user(subject, message)
			return redirect('account_activation_sent')
		else:
			errors = []
			for error_key in form.errors.keys():
				errors.append(form.errors[error_key])
			request.session['errors'] = errors
			return redirect('registration_result')
	else:
		form = RegistrationForm()
	return render(request, 'WebApp/registration.html', {'form': form})

# This view shows the registration result
def registration_result(request):
	return render(request, 'WebApp/registration_result.html', {'errors': request.session.get('errors')})

# This view handles the activiation of account
def activate(request, uidb64, token):
	b64 = force_bytes(uidb64)
	uidb = urlsafe_base64_decode(b64)
	uid = force_text(uidb)
	try:
		user = CustomUser.objects.get(pk = uid)
	except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.is_email_confirmed = True
		user.save()
		login(request, user)
		request.session['errors'] = []
		return redirect('registration_result')
	else:
		return render(request, 'WebApp/account_activation_invalid.html', {'uidb64': uidb64, 'b64': b64, 'uidb': uidb, 'uid': uid})

def account_activation_sent(request):
	return render(request, 'WebApp/account_activation_sent.html')