from rest_framework import serializers\

from .models import Merchant
from accounts.serializer import AccountSerializer


class MerchantSerializer(serializers.ModelSerializer):
    accounts = AccountSerializer(read_only=True, many=True)

    class Meta:
        model = Merchant
        fields = ('uuid', 'name', 'accounts')
