from conductoresApp.models import Conductor
from rest_framework import serializers

class ConductorSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Conductor
        fields = '__all__'