from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static


api_urlpatterns = [
    url(r'^auth/', include('auth.urls')),
    url(r'^users/', include('users.urls')),
    url(r'^tasks/', include('tasks.urls')),
    url(r'^notifications/', include('notifications.urls'))

]

urlpatterns = [
    url(r'^v1/', include(api_urlpatterns)),
    url(r'^admin/', admin.site.urls),
    url(r'^docs/', include('rest_framework_swagger.urls')),
]

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL,
#                           document_root=settings.STATIC_ROOT)
