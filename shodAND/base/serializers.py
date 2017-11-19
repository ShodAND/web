from rest_framework import seralizers

from .models import Host

class HostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Host
        fields = ('hostname', 'ip', 'creation_date', 'modification_date')
