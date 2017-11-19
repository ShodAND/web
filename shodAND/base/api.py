from rest_framework import viewsets

from .models import Host, Port
from .serializers import HostSerializer, PortSerializer

class HostAPI(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Host.objects.all().order_by('-creation_date')
    serializer_class = HostSerializer

class PortAPI(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Port.objects.all().order_by('-creation_date')
    serializer_class = PortSerializer
