from rest_framework import serializers
from .models import Host, Port

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('hostname', 'ip', 'creation_date', 'modification_date')

class PortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Port
        fields = ('port', 'creation_date', 'modification_date')
