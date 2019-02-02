from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Account


@admin.register(Account)
class AccountAdmin(UserAdmin):

    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('display_name', 'email', 'balance')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 'email', 'display_name', 'balance', 'is_staff')
    search_fields = ('username', 'display_name', 'email')
    filter_horizontal = ('groups', 'user_permissions')
