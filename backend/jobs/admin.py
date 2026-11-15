from django.contrib import admin

# Register your models here.
from .models import Job, Profile

admin.site.register(Job)
admin.site.register(Profile)