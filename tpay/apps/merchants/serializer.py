from rest_framework import serializers

from .models import Merchant
from accounts.models import Account
from media_upload.serializer import ImageSerializer


class MerchantAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('id', 'username', 'email')


class MerchantSerializer(serializers.ModelSerializer):
    accounts = MerchantAccountSerializer(read_only=True, many=True)
    icon = ImageSerializer()

    class Meta:
        model = Merchant
        fields = ('id', 'name', 'accounts', 'icon')
