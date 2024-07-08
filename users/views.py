from django.http import HttpRequest
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.shortcuts import render
import time

from .models import User


@api_view(http_method_names=["POST"])
def login(request: HttpRequest):
    username = request.data.get("username")
    password = request.data.get("password")
    user = User.objects.filter(username=username)
    if not user:
        return Response({
            "status": "error",
            "errors": {
                "username": "username not found",
            },
            "data": {},
        })
    user = user.first()
    check_password = user.check_password(raw_password=password)
    if not check_password:
        return Response({
            "status": "error",
            "errors": {
                "password": "Password is invalid",
            },
            "data": {},
        })
    token = Token.objects.get_or_create(user=user)
    return Response({
        "status": "success",
        "errors": {},
        "data": {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "token": token[0].key,
        }
    })
