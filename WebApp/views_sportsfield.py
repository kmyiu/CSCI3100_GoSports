from django.db.models import Field
from django.shortcuts import render, redirect, get_object_or_404
from .models import SportsField, CustomUser
from .forms import SportsFieldCommentForm

# This view handles the sportsfields list
def sportsfield_list(request):
	fields_base_name =  ['name', 'belongs_to', 'rate', 'sports_type', 'id']
	fields = [field for field in SportsField._meta.get_fields() if field.name in fields_base_name]
	sportsfields = []
	sportsfields_base = SportsField.objects.all().order_by('name')
	for sportsfield_base in sportsfields_base:
		sportsfield = {}
		for field in fields:
			sportsfield[field.verbose_name] = sportsfield_base.__getattribute__(field.name)
		sportsfields.append(sportsfield)
	return render(request, 'WebApp/sportsfield_list.html', {'sportsfields': sportsfields})

# This view handles the sportsfields details
def sportsfield_detail(request, pk):
	sportsfield_base = get_object_or_404(SportsField, pk = pk)
	sportsfield = {}
	if sportsfield_base:
		fields_base_name =  ['name', 'opening_hour', 'can_be_booked', 'need_membership', 'is_free', 'payment_detail', 'is_indoor', 'id', 'rate', 'sports_type', 'remark', 'belongs_to']
		fields = [field for field in SportsField._meta.get_fields() if field.name in fields_base_name]
		for field in fields:
			sportsfield[field.verbose_name] = sportsfield_base.__getattribute__(field.name)
	return render(request, 'WebApp/sportsfield_detail.html', {'sportsfield': sportsfield, 'comments': sportsfield_base.CommentTargetedSportsField.reverse()})

# This view handles the comment function
def comment(request, pk):
	if request.method == 'POST':
		form = SportsFieldCommentForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('comment_result')
	else:
		sportsfield = SportsField.objects.get(pk = pk)
		user = CustomUser.objects.get(username = request.user.username)
		form = SportsFieldCommentForm(initial = {'target_sportsfield': sportsfield, 'commenter': user})
	return render(request, 'WebApp/comment.html', {'form': form})

# This view handles the comment results
def comment_result(request):
	return render(request, 'WebApp/comment_result.html')