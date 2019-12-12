from django.db.models import Field
from django.shortcuts import render, redirect, get_object_or_404
from .models import Facility

# This view handles the facilities list
def facility_list(request):
	fields_base_name =  ['name', 'district', 'rate', 'sports_type', 'id']
	fields = [field for field in Facility._meta.get_fields() if field.name in fields_base_name]
	facilities = []
	facilities_base = Facility.objects.all().order_by('name')
	for facility_base in facilities_base:
		facility = {}
		for field in fields:
			facility[field.verbose_name] = facility_base.__getattribute__(field.name)
		facilities.append(facility)
	return render(request, 'WebApp/facility_list.html', {'facilities': facilities})

# This view handles the facility details
def facility_detail(request, pk):
	facility_base = get_object_or_404(Facility, pk = pk)
	facility = {}
	if facility_base:
		fields_base_name =  ['name', 'district', 'address', 'rate', 'latitude', 'longitude', 'sports_type', 'id', 'remark']
		fields = [field for field in Facility._meta.get_fields() if field.name in fields_base_name]
		for field in fields:
			facility[field.verbose_name] = facility_base.__getattribute__(field.name)
	return render(request, 'WebApp/facility_detail.html', {'facility': facility})