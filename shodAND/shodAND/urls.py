from django.conf.urls import url, include
from django.contrib import admin
from base import api

urlpatterns = [
    url(r'^api/v1/', include(api.routes.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^base/', include('base.urls')),
]
