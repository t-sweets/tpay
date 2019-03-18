from rest_framework import serializers

from .models import Transfer
from accounts.models import Account
from accounts.serializer import AccountSerializer


class TransferSerializer(serializers.ModelSerializer):
    user_from = AccountSerializer(read_only=True)
    user_to = AccountSerializer(read_only=True)
    user_to_id = serializers.CharField(max_length=255, write_only=True)

    class Meta:
        model = Transfer
        fields = ('id', 'created_time', 'amount', 'user_from', 'user_to', 'user_to_id', 'message')

    def create(self, validated_data):
        validated_data['user_to'] = Account.objects.get(username=validated_data.pop('user_to_id', None))
        if validated_data['user_to'] is None:
            raise serializers.ValidationError("user not found.")
        validated_data['user_from'] = self.context['request'].user
        return Transfer.objects.transfer(request_data=validated_data)
