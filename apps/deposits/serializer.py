from rest_framework import serializers

from .models import Deposit


class DepositSerializer(serializers.ModelSerializer):
    idm = serializers.CharField(max_length=16, write_only=True)

    class Meta:
        model = Deposit
        fields = ('id', 'created_time', 'updated_time', 'amount', 'idm')

    def create(self, validated_data):
        return Deposit.objects.deposit(request_data=validated_data)
