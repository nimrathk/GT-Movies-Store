from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    # Optionally, specify the fields you want to display:
    fields = ('security_question', 'security_answer')

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

# Unregister the original User admin and register the new one
admin.site.unregister(User)
admin.site.register(User, UserAdmin)