from rest_framework import serializers

from .models import Model, Face, Worker

class ModelSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%m-%d %H:%M:%S")
    class Meta:
        model = Model
        fields = ("camera_id", "created", "number_of_people", "image", "type", )


class WorkerModelSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%m-%d %H:%M:%S")
    class Meta:
        model = Worker
        fields = ("id", "uuid", "fullname", "image", "created", )


class FaceModelSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(format="%m-%d %H:%M:%S")
    worker = WorkerModelSerializer(Worker, many=False)
    class Meta:
        model = Face
        fields = ("type", "image", "created", "worker", )
