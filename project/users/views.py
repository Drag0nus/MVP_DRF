from datetime import datetime, timedelta
from rest_framework import mixins, viewsets, status, permissions
from rest_framework.response import Response

from common.drf.mixins import ActionPermissionClassesMixin
from common.drf.permissions import NotAuthenticated
from users.tasks import make_file, get_weather

from .serializers import UserSerializer
from .models import User

from notifications.tasks import congratz_after_30days


class UserViewSet(ActionPermissionClassesMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    model = User
    queryset = User.objects.all()
    serializer_class = UserSerializer

    action_permission_classes = {
        'create': [NotAuthenticated],
        'retrieve': [permissions.IsAuthenticated],
        'update': [permissions.IsAuthenticated],
        'partial_update': [permissions.IsAuthenticated],
        'destroy': [permissions.IsAuthenticated],
    }

    def get_object(self):
        return self.request.user

    def get_queryset(self):
        return User.objects.all()

    def get_serializer_class(self):
        return super(UserViewSet, self).get_serializer_class()

    def destroy(self, request, *args, **kwargs):
        if request.user.check_password(request.data.get('password')):
            request.get_object.deactivate()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)

    def create(self, request, *args, **kwargs):
        """
        Main Info.
        ---
        omit_serializer: false
        parameters:
          - name: email
            required: true
            type: string
          - name: password
            required: true
            type: string
          - name: first_name
            type: string
          - name: last_name
            type: string
          - name: about
            type: string
          - name: avatar
            type: file
        """

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        congratz_after_30days.apply_async(eta=datetime.now() + timedelta(seconds=10),
                                          args=[serializer.data.get('id')])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(instance, '_prefetched_objects_cache', None):
            # If 'prefetch_related' has been applied to a queryset, we need to
            # refresh the instance from the database.
            instance = self.get_object()
            serializer = self.get_serializer(instance)
        print(serializer.data['id'])
        get_weather.delay(serializer.data['id'])
        return Response(serializer.data)
