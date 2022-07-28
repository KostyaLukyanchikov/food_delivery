from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import forms
from . import models


class CustomUserAdmin(UserAdmin):
    add_form = forms.CustomUserCreationForm
    form = forms.CustomUserChangeForm
    model = models.CustomUser
    list_display = ('username', 'balance')
    fieldsets = (
        (None, {'fields': ('username', 'password', 'balance')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
            )
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')})
    )


admin.site.register(models.CustomUser, CustomUserAdmin)
