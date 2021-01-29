from django.contrib import admin
from .models import User_Details
from .models import next_run_time
# Register your models here.

admin.site.register(User_Details)
admin.site.register(next_run_time)
