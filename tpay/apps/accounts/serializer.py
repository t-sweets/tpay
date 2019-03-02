from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Account, Idm


class IdmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idm
        fields = ('id', 'idm', 'name')
        extra_kwargs = {
            'idm': {'write_only': True},
        }

    def create(self, validated_data):
        account = get_object_or_404(Account, pk=self.context['request'].user.id)
        obj = Idm.objects.create(**validated_data, account=account)
        obj.save()
        return obj


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
