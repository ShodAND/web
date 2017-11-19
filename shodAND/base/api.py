from rest_framework import viewsets

from .models import Host
from .serializers import HostSerializer

class HostAPI(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Host.objects.all().order_by('-creation_date')
    serializer_class = HostSerializer
