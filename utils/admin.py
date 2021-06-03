from django.contrib import admin

from django.contrib.auth.models import User
from utils.models import UserProfile

# Register your models here.


class UserProfileAdmin(admin.ModelAdmin):
    model = UserProfile

admin.site.register(UserProfile, UserProfileAdmin) 