from django.db.models import Field
from django.shortcuts import render, redirect
from .forms import *
from .models import CustomUser, Facility

# This view handles the advance search function
def advanced_search(request):
	return render(request, 'WebApp/advanced_search.html')

# This view handles the advance search results
def advanced_search_result(request):
	results = []
	search_type = ''
	if request.method == 'POST':
		search_type = request.POST['search_type']
		if search_type == 'facility':
			results_base = Facility.objects.all()
		else:
			results_base = CustomUser.objects.all()
		kwargs = {field_name: field_value for field_name, field_value in request.POST.items() if field_name != 'search_type' and field_name != 'csrfmiddlewaretoken' and field_value != ''}
		if kwargs:
			results_base = results_base.filter(**kwargs)
			if search_type == 'facility':
				results_base = results_base.order_by('-rate')
				fields_base = Facility._meta.get_fields()
			else:
				results_base = results_base.order_by('username')
				fields_base = User._meta.get_fields()
			fields = [field for field in fields_base if isinstance(field, Field) and field.verbose_name != '']
			for result_base in results_base:
				result = {}
				for field in fields:
					result[field.verbose_name] = result_base.__getattribute__(field.name)
				results.append(result)
	return render(request, 'WebApp/search_result.html', {'results': results})

# This view handles the search results
def search_result(request):
	results = []
	if request.method == "POST":
		search_type = request.POST['search_type']
		if search_type == 'facility':
			results_base = Facility.objects.all()
		else:
			results_base = CustomUser.objects.all()
		kwargs = {field_name: field_value for field_name, field_value in request.POST.items() if field_name != 'search_type' and field_name != 'csrfmiddlewaretoken'}
		results_base = results_base.filter(**kwargs)
		if search_type == 'facility':
			results_base = results_base.order_by('-rate')
			fields_base = Facility._meta.get_fields()
		else:
			results_base = results_base.order_by('username')
			fields_base = User._meta.get_fields()
		fields = [field for field in fields_base if isinstance(field, Field) and field.verbose_name != '']
		for result_base in results_base:
			result = {}
			for field in fields:
				result[field.verbose_name] = result_base.__getattribute__(field.name)
			results.append(result)
		return render(request, 'WebApp/search_result.html', {'results': results, 'fields': fields})
	else:
		return redirect('homepage')