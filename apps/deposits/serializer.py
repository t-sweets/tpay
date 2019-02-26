from rest_framework import serializers

from .models import Deposit


class DepositSerializer(serializers.ModelSerializer):
    idm = serializers.CharField(max_length=16, write_only=True)

    class Meta:
        model = Deposit
        fields = ('id', 'created_time', 'updated_time', 'amount', 'idm')

    def create(self, validated_data):
        validated_data['merchant'] = validated_data.pop('merchant_id', None)
        if validated_data['merchant'] is None:
            raise serializers.ValidationError("merchant not found.")
        if self.context['request'].user not in validated_data['merchant'].accounts.all():
            raise serializers.ValidationError("merchant not in auth user.")
        return Deposit.objects.deposit(request_data=validated_data)
