from rest_framework import serializers
from .models import Host

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('hostname', 'ip', 'creation_date', 'modification_date')
