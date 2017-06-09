from rest_framework import mixins, viewsets, status, permissions
from rest_framework.response import Response

from common.drf.mixins import ActionPermissionClassesMixin
from common.drf.permissions import NotAuthenticated

from notifications.serializers import NotificationSerializer
from notifications.models import Notification


class NotificationViewSet(mixins.RetrieveModelMixin,
                          mixins.UpdateModelMixin,
                          mixins.DestroyModelMixin,
                          mixins.CreateModelMixin,
                          mixins.ListModelMixin,
                          viewsets.GenericViewSet):
    model = Notification
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

    # action_permission_classes = {
    #     'create': [NotAuthenticated],
    #     'retrieve': [permissions.IsAuthenticated],
    #     # 'update': [permissions.IsAuthenticated],
    #     # 'partial_update': [permissions.IsAuthenticated],
    #     'update': [NotAuthenticated],
    #     'partial_update': [NotAuthenticated],
    #     'destroy': [permissions.IsAuthenticated],
    # }
