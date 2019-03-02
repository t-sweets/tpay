from rest_framework import serializers
from checkouts.serializer import CheckoutMerchantSerializer


class TransactionSerializer(serializers.Serializer):
    id = serializers.CharField()
    amount = serializers.SerializerMethodField()
    created_time = serializers.DateTimeField()
    merchant = CheckoutMerchantSerializer()
    type = serializers.CharField()

    def get_amount(self, obj):
        return obj.cash_value()
