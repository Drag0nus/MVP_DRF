from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers


class TokenSerializer(serializers.Serializer):
    access_token = serializers.CharField(max_length=256)
    refresh_token = serializers.CharField(max_length=256)
    token_type = serializers.CharField(max_length=256)
    expires_in = serializers.IntegerField()
    scope = serializers.CharField(max_length=256)


class RequestTokenSerializer(serializers.Serializer):
    client_id = serializers.CharField(max_length=256)
    client_secret = serializers.CharField(max_length=500)
    grant_type = serializers.CharField(max_length=256)

    refresh_token = serializers.CharField(max_length=256, required=False)
    username = serializers.EmailField(max_length=256, required=False,
                                      help_text='User email address.')
    password = serializers.CharField(max_length=256, required=False)

    def validate(self, attrs):
        email = attrs.get('username')
        password = attrs.get('password')

        if email and password:
            user = authenticate(email=email, password=password)

            if user:
                if not user.is_active:
                    msg = _('User account is disabled.')
                    raise serializers.ValidationError(msg)
            else:
                msg = _('Unable to log in with provided credentials.')
                raise serializers.ValidationError(msg)
        else:
            msg = _('Must include "username" and "password".')
            raise serializers.ValidationError(msg)

        attrs['user'] = user
        return attrs


class RequestRevokeTokenSerializer(serializers.Serializer):
    client_id = serializers.CharField(max_length=256, help_text='Client id')
    client_secret = serializers.CharField(max_length=500,
                                          help_text='Client secret')
    token = serializers.CharField(max_length=256, help_text='Access token')