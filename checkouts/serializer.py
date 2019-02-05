from rest_framework import serializers

from .models import Checkout


class CheckoutSerializer(serializers.ModelSerializer):
    idm = serializers.CharField(max_length=16, write_only=True)

    class Meta:
        model = Checkout
        fields = ('uuid', 'created_time', 'updated_time', 'amount', 'merchant', 'idm', 'payment_method')

    def create(self, validated_data):
        return Checkout.objects.checkout(request_data=validated_data)
