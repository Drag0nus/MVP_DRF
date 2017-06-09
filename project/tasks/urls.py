from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from tasks.views import TaskViewSet

router = DefaultRouter()
router.register('tasks', TaskViewSet, base_name='tasks-tasks')

urlpatterns = [
    url(r'^', include(router.urls))
]
