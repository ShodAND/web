from django.contrib import admin
from .models import Host, Port, Scan

admin.site.register(Host)
admin.site.register(Port)
admin.site.register(Scan)
