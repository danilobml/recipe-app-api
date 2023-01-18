from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


class UserAdmin(BaseUserAdmin):
    """ Defines custom user admin, using django's base class for config (UserAdmin em django.contrib.auth.admin)"""
    ordering = ['id']
    list_display = ['email', 'name']
    """ Enables the display, ordered by id"""
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser'
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)})
    )
    readonly_fields = ['last_login']


admin.site.register(models.User, UserAdmin)
""" Register the changes, using this class UserAdmin"""
