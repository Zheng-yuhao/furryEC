from django.shortcuts import render
from . import serializer
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.decorators import action
from furryEC.utils.response import APIResponse
from furryEC.libs import aws_ses
from furryEC.utils.logger import log
from django.core.cache import cache
import re
from . import models
from .throttings import SMSThrotting

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
            return APIResponse(code=0, msg=ser.errors)

    @action(methods=['GET'], detail=False)
    def send_email(self, request, *args, **kwargs):
        email = request.query_params.get('email')  # for the test
        confirmation_code = aws_ses.get_code()
        try:
            re = aws_ses.send(ToAddresses='nikaitosuzu@gmail.com', Sub_Data='Test Subject', code=confirmation_code)
            if re.get('MessageId'):
                cache.set('email', email)
                cache.set('code', confirmation_code)
                return APIResponse(code=100, msg='We have already sent you a confirmation email')
            else:
                return APIResponse(code=0, msg='Invalid error, please contact the administrator.')
        except Exception as e:
            log.error(e)

    @action(methods=['GET'], detail=False)
    def check_email(self, request, *args, **kwargs):
        email = request.query_params.get('email')
        print(email)
        if not email:
            return APIResponse(code=0, msg='Please send the email only.')
        if not re.match('^.+@.+$', email):
            print('here')
            return APIResponse(code=0, msg='The email format is wrong.')
        try:
            models.User.objects.get(email=email)
            return APIResponse(code=1, msg='Success')
        except:
            return APIResponse(code=0, msg='Email address invalid')

    # After completing the AWS SMS api process.
    @action(methods=['POST'], detail=False)
    def code_login(self, request, *args, **kwargs):
        ser = serializer.CodeUserSerializer(data=request.data)
        if ser.is_valid():
            token = ser.context['token']
            username = ser.context['user']
            return APIResponse(token=token, username=username)
        else:
            return APIResponse(code=0, msg=ser.errors)


class SignUpView(GenericViewSet, CreateModelMixin):
    queryset = models.User.objects.all()
    serializer_class = serializer.SignUpSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs) # response是一个Response对象->看源码
        username = response.data.get('username')
        print(response.data)
        return APIResponse(code=1, msg='Create New user Successfully', username=username)
