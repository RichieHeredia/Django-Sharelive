from django.contrib import admin
from basic_app.models import UserProfileInfo
from .models import API 

# Register your models here.

admin.site.register(UserProfileInfo)
admin.site.register(API)