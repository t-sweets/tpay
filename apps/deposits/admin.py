from django.contrib import admin
from .models import Deposit


@admin.register(Deposit)
class DepositAdmin(admin.ModelAdmin):
    list_display = ('id', 'created_time', 'amount', 'merchant', 'user')
