from rest_framework import serializers
from .models import User


class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)
    balance = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'display_name', 'balance', 'password')

    def create(self, validated_data):
        return User.objects.create_user(request_data=validated_data)

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            instance.set_password(validated_data['password'])
        else:
            instance = super().update(instance, validated_data)
        instance.save()
        return instance
