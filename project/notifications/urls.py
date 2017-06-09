from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from notifications.views import NotificationViewSet

router = DefaultRouter()
router.register('tasks', NotificationViewSet, base_name='notifications')

urlpatterns = [
    url(r'^', include(router.urls))
]