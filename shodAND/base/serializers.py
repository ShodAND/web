from rest_framework import serializers
from .models import Host, Port, Scan

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('hostname', 'ip', 'creation_date', 'modification_date')

class PortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Port
        fields = ('port', 'label', 'privileged', 'creation_date', 'modification_date')

class ScanSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scan
        fields = ('host', 'ports', 'creation_date', 'modification_date')
