from django.shortcuts import render
from . import serializer
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from furryEC.utils.response import APIResponse

# Create your views here.


class LoginView(ViewSet):

    @action(methods=['POST'], detail=False)
    def login(self, request, *args, **kwargs):
        ser = serializer.LoginSer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user']
            return APIResponse(token=token, username=username)
        else:
            return APIResponse(code='0', msg=ser.errors)
