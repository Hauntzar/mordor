from rest_framework import serializers
from .models import Event,EventData


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=Event
        fields = '__all__'

class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model=EventData
        fields = '__all__'