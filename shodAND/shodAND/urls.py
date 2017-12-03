from django.conf.urls import url, include
from django.contrib import admin
from base import api
from django.views import generic
from material.frontend import urls as frontend_urls

urlpatterns = [
    url(r'^api/v1/', include(api.routes.urls)),
    #url(r'^admin/', admin.site.urls),
    url(r'^base/', include('base.urls')),
    url(r'^$', generic.RedirectView.as_view(url='/workflow/', permanent=False)),
    url(r'', include(frontend_urls)),
]
