from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    # address = UserAddressSerializer(required=True)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
        # fields='__all__'


class UserAddressSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    state = serializers.StringRelatedField()
    city = serializers.StringRelatedField()

    class Meta:
        model = UserAddress
        fields = '__all__'

    def create(self, validated_data):

        user_data = validated_data.pop('user')
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        Detail, created = UserAddress.objects.update_or_create(user=user,
                                                               state=validated_data.pop('state'),
                                                               city=validated_data.pop('city'),
                                                               locality=validated_data.pop('locality'),
                                                               house=validated_data.pop('house'),
                                                               landmark=validated_data.pop('landmark'),
                                                               phone=validated_data.pop('phone'),
                                                               blood=validated_data.pop('blood'),
                                                               birth=validated_data.pop('birth'),
                                                               gender=validated_data.pop('gender'),
                                                               )

        return Detail


