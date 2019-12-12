'''
The forms file stores the form of updating information. 
'''

from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from datetime import date

year_now = date.today().year
YEARS = list(range(year_now, 1940, -1))
YEARS2 = list(range(year_now, year_now+3))

# This form handles the registration function
# The clean_password1/2 handles the validation of passwords
class RegistrationForm(forms.ModelForm):
	password1 = forms.CharField(label = 'Password', widget = forms.PasswordInput, help_text = 'Required.<ul3><li>Your password cannot be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password cannot be a commonly used password.</li><li>Your password cannot be entirely numeric.</li></ul>')
	password2 = forms.CharField(label = 'Password confirmation', widget = forms.PasswordInput, help_text = 'Enter the same password as before, for verification.')
	email1 = forms.CharField(label = 'Email address', max_length = 255, widget = forms.EmailInput, help_text = 'Required. Please enter a valid email address. An activiation email would be sent to this email.')
	email2 = forms.CharField(label = 'Email address confirmation', max_length = 255, widget = forms.EmailInput, help_text = 'Enter the same email address as before, for verification.')
	class Meta:
		model = CustomUser
		fields = ('username', 'first_name', 'last_name', 'date_of_birth', 'gender', 'interest', )

	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.fields['date_of_birth'].widget = forms.SelectDateWidget(years = YEARS, empty_label = ('-- Year --', '-- Month --', '-- Day --'))

	def clean_password2(self):
		password1 = self.cleaned_data.get("password1")
		password2 = self.cleaned_data.get("password2")
		if password1 and password2 and password1 != password2:
			raise forms.ValidationError("Passwords don't match.")
		return password2

	def clean_email2(self):
		email1 = self.cleaned_data.get("email1")
		email2 = self.cleaned_data.get("email2")
		if email1 and email2 and email1 != email2:
			raise forms.ValidationError("Emails don't match.")
		return email2

	def save(self, commit = True):
		user = super().save(commit = False)
		user.set_password(self.cleaned_data["password1"])
		user.email = self.cleaned_data["email1"]
		user.nickname = self.cleaned_data["username"]
		user.is_active = False
		if commit:
			user.save()
		return user

# This form handles the profile editing function
class ProfileEditForm(forms.ModelForm):
	class Meta:
		model = CustomUser
		fields = ('first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'interest', 'self_introduction', 'propic', )
	def __init__(self, *args, **kwargs):
		super(ProfileEditForm, self).__init__(*args, **kwargs)
		self.fields['date_of_birth'].widget = forms.SelectDateWidget(years = YEARS, empty_label = ('-- Year --', '-- Month --', '-- Day --'))
	def save(self, commit = False):
		return super().save(commit = False) 

# This form handles the advanced search function
class AdvancedSearchForm(forms.ModelForm):
	class Meta:
		model = Facility
		fields = ('name', 'district', 'sports_type', )

# This form handles the facilities advanced search function
class FacilityAdvancedSearchForm(forms.ModelForm):
	class Meta:
		model = Facility
		fields = ('name', 'district', 'sports_type', )

# This form handles the sportsfield advanced search function
class SportsFieldAdvancedSearchForm(forms.ModelForm):
	class Meta:
		model = SportsField
		fields = ('sports_type', 'is_free', 'is_indoor', )#'name', )

# This form handles the commenting sportsfield function
class SportsFieldCommentForm(forms.ModelForm):
	class Meta:
		model = CommentOnSportsField
		fields = ('commenter', 'comment', 'rate', 'target_sportsfield', )
	def save(self, commit = True):
		comment = super().save(commit = False)
		if commit:
			target_sportsfield = comment.target_sportsfield
			target_sportsfield.rate_numerator += comment.rate
			target_sportsfield.rate_denominator += 1
			# calculate the updated rate every time on update
			raw_rate = target_sportsfield.rate_numerator / target_sportsfield.rate_denominator
			# format the rate and pass it back as a string
			target_sportsfield.rate = "{0:.2f}".format(raw_rate)
			comment.save()
			target_sportsfield.save()
		return comment

# This form handles the appointment function
class AppointmentForm(forms.ModelForm):
	class Meta:
		model = Appointment
		fields = ('appointment_time', 'sports_type', 'location', 'max_num', 'remark',)

	def __init__(self, *args, **kwargs):
		super(AppointmentForm, self).__init__(*args, **kwargs)
		self.fields['appointment_time'].widget = forms.SelectDateWidget(years=YEARS2)