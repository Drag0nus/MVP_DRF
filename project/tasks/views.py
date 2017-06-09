from rest_framework import mixins, viewsets, status, permissions
from rest_framework.decorators import list_route
from rest_framework.response import Response

from common.drf.mixins import ActionPermissionClassesMixin
from common.drf.permissions import NotAuthenticated

from .serializers import TaskSerializer
from .models import Task


class TaskViewSet(ActionPermissionClassesMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    model = Task
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    @list_route(methods=['get'], url_path='stats')
    def task_counter(self, request):
        queryset = Task.objects.all()
        return Response(queryset.count())

    action_permission_classes = {
        # 'create': [NotAuthenticated],
        # 'retrieve': [permissions.IsAuthenticated],
        # 'update': [permissions.IsAuthenticated],
        # 'partial_update': [permissions.IsAuthenticated],
        # 'destroy': [permissions.IsAuthenticated],
        'create': [NotAuthenticated],
        'retrieve': [NotAuthenticated],
        'update': [NotAuthenticated],
        'partial_update': [NotAuthenticated],
        'destroy': [NotAuthenticated],
    }
    #
    # def create(self, request, *args, **kwargs):
    #     """
    #     Create Task
    #     ---
    #     omit_serializer: true
    #     parameters:
    #       - name: task_title
    #         required: true
    #         type: # string
    #       - name: task_description
    #         type: # string
    #       - name: author
    #         required: True
    #
    #
    #     """
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     headers = self.get_success_headers(serializer.data)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)