from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'email', 'password', 'first_name', 'last_name', 'gender', 'city', 'weather', 'about',
                  'date_joined', 'is_active', 'is_staff', 'avatar']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True,
                         'required': True},
            'email': {'required': True},
            'first_name': {'required': True},
            'last_name': {'required': True},
            # 'gender': {'read_only': True},
            'date_joined': {'read_only': True},
            'is_active': {'read_only': True},
            'is_staff': {'read_only': True},
            'weather': {'read_only': True},
        }

    def update(self, instance, validated_data):
        if validated_data.get('password'):
            instance.set_password(validated_data.pop('password'))
        return super(UserSerializer, self).update(instance, validated_data)
