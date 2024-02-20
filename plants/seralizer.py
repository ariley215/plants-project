from rest_framework import serializers
from .models import Plant

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = [
            "id",
            "owner",
            "name",
            "scientific_name",
            "bloom_time", 
            "description",
            "flower_color",
            "created_at",
            "updated_at",
        ]
