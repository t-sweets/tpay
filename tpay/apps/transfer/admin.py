from django.contrib import admin
from .models import Transfer


@admin.register(Transfer)
class MerchantAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_time', 'updated_time', 'user_from', 'user_to', 'amount')
