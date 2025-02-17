from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin

# Register your models here.
class CustomUserAdmin(DefaultUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)