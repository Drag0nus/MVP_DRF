from rest_framework import serializers
# from users.models import User
from notifications.models import Notification


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user_notified', 'text', 'notification_date']

        extra_kwargs = {
            'id': {'read_only': True},
            'text': {'required': True},
            'notification_date': {'read_only': True}
        }
