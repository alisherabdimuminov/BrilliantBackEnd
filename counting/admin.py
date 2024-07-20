from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Model, Face, Worker


@admin.register(Model)
class InputModelAdmin(ModelAdmin):
    list_display = ["camera_id", "created", "number_of_people", "type", ]


@admin.register(Face)
class FaceModelAdmin(ModelAdmin):
    list_display = ["type", "worker", "created", ]


@admin.register(Worker)
class WorkerModelAdmin(ModelAdmin):
    list_display = ["uuid", "fullname", "created", ]
