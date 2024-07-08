from django.contrib import admin
from unfold.admin import ModelAdmin
from django.contrib.auth.forms import UserCreationForm

from .models import User
from .forms import UserModelChangeForm


@admin.register(User)
class User(ModelAdmin):
    add_form = UserCreationForm
    form = UserModelChangeForm
    list_display = ["username", "first_name", "last_name"]
    add_fieldsets = (
        ("Foydalanuvchi qo'shish", {
            "fields": ("username", "password1", "password2", "first_name", "last_name", ),
        }),
    )
    fieldsets = (
        ("Foydalanuvchini tahrirlash", {
            "fields": ("username", "first_name", "last_name", ),
        }),
    )
    