from rest_framework import serializers
from .models import Box

class BoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = Box
        fields = ['id', 'length', 'breadth', 'height']

class BoxListSerializer(serializers.ModelSerializer):
    area = serializers.ReadOnlyField()
    volume = serializers.ReadOnlyField()
    created_by = serializers.CharField(source='created_by.username', read_only=True)
    last_updated = serializers.DateTimeField(source='updated_at', read_only=True)

    class Meta:
        model = Box
        fields = ['id', 'length', 'breadth', 'height', 'area', 'volume', 'created_by', 'last_updated']
