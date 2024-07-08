from django.contrib import admin
from unfold.admin import ModelAdmin

from .models import Model


@admin.register(Model)
class InputModelAdmin(ModelAdmin):
    list_display = ["camera_id", "created", "number_of_people", "type", ]
