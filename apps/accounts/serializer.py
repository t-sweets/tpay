from rest_framework import serializers
from .models import Account, Idm


class IdmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idm
        fields = ('idm', 'account')
        extra_kwargs = {
            'idm': {'write_only': True},
            'account': {'write_only': True},
        }


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    balance = serializers.CharField(read_only=True)

    class Meta:
        model = Account
        fields = ('username', 'email', 'display_name', 'balance', 'password')

    def create(self, validated_data):
        return Account.objects.create_user(request_data=validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance
