from rest_framework import serializers

from .models import Model

class ModelSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%m-%d %H:%M:%S")
    class Meta:
        model = Model
        fields = ("camera_id", "created", "number_of_people", "image", "type", )
