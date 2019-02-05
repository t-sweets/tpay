from django.contrib import admin
from .models import Checkout


@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display = ('uuid', 'created_time', 'updated_time', 'amount', 'payment_method', 'merchant')
