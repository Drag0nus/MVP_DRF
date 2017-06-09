from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from common.drf.routers import NoLookupFieldRouter
from users.views import UserViewSet

# router = NoLookupFieldRouter(trailing_slash=False)
router = DefaultRouter()
# router = DefaultRouter(trailing_slash=False)
router.register('users', UserViewSet, base_name='users-users')

urlpatterns = [
    url(r'^', include(router.urls)),
]
