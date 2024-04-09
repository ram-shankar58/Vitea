from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group


User = get_user_model() 

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'campus', 'phone_no', 'regno', 'year', 'description')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'campus', 'phone_no', 'regno')
    ordering = ('username',)

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (('Personal info'), {'fields': ('first_name', 'last_name', 'email', 'campus', 'phone_no', 'regno', 'description')}),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
admin.site.register(User, CustomUserAdmin)