from rest_framework import serializers

from .models import Checkout


class CheckoutSerializer(serializers.ModelSerializer):
    idm = serializers.CharField(max_length=16, write_only=True)

    class Meta:
        model = Checkout
        fields = ('id', 'created_time', 'amount', 'merchant', 'idm', 'payment_method')
        extra_kwargs = {
            'payment_method': {'write_only': True},
        }

    def create(self, validated_data):
        return Checkout.objects.checkout(request_data=validated_data)
