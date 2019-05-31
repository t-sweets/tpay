from rest_framework import serializers
from django.shortcuts import get_object_or_404

from .models import Account, Idm
from media_upload.serializer import ImageSerializer
from media_upload.models import Image


class IdmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idm
        fields = ('id', 'idm', 'name')

    def create(self, validated_data):
        account = get_object_or_404(Account, pk=self.context['request'].user.id)
        obj = Idm.objects.create(**validated_data, account=account)
        obj.save()
        return obj


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    balance = serializers.CharField(read_only=True)
    icon = ImageSerializer(read_only=True)
    icon_id = serializers.PrimaryKeyRelatedField(queryset=Image.objects.all(), write_only=True, required=False)

    class Meta:
        model = Account
        fields = ('username', 'email', 'display_name', 'balance', 'password', 'icon', 'icon_id')

    def create(self, validated_data):
        return Account.objects.create_user(request_data=validated_data)

    def update(self, instance, validated_data):
        if 'icon_id' in validated_data:
            validated_data['icon'] = validated_data.pop('icon_id', None)
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance
