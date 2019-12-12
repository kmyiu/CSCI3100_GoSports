from django.contrib import admin
from .models import *

# Allow administrator to manage the databases
admin.site.register(CustomUser)
admin.site.register(Facility)
admin.site.register(SportsField)
admin.site.register(CommentOnSportsField)
admin.site.register(Appointment)