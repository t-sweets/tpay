from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Checkout
from merchants.models import Merchant
from media_upload.serializer import ImageSerializer


class CheckoutMerchantSerializer(serializers.ModelSerializer):
    icon = ImageSerializer()

    class Meta:
        model = Merchant
        fields = ('name', 'icon')


class CheckoutSerializer(serializers.ModelSerializer):
    idm = serializers.CharField(max_length=16, write_only=True)
    merchant = CheckoutMerchantSerializer(read_only=True)
    merchant_id = serializers.PrimaryKeyRelatedField(queryset=Merchant.objects.all(), write_only=True)

    class Meta:
        model = Checkout
        fields = ('id', 'created_time', 'amount', 'merchant', 'merchant_id', 'idm', 'payment_method')
        extra_kwargs = {
            'payment_method': {'write_only': True},
        }

    def create(self, validated_data):
        validated_data['merchant'] = validated_data.pop('merchant_id', None)
        if validated_data['merchant'] is None:
            raise serializers.ValidationError("merchant not found.")
        if self.context['request'].user not in validated_data['merchant'].accounts.all():
            raise serializers.ValidationError("merchant not in auth user.")
        return Checkout.objects.checkout(request_data=validated_data)
