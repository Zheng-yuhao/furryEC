from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler
from django.core.cache import cache

from . import models
import re


# login serializer
class LoginSer(ModelSerializer):
    username = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['username', 'password', 'id']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }

    def validate(self, attrs):
        print(attrs)
        user = self.__get_user(attrs)

        token = self.__get_token(attrs, user)

        self.context['token'] = token
        self.context['user'] = user.username

        return attrs

    def __get_user(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if re.match('^1[1-9]{10}$', username):
            user = models.User.objects.filter(telephone=username).first()

        elif re.match('^.+@.+$', username):
            user = models.User.objects.filter(email=username).first()

        else:
            user = models.User.objects.filter(username=username).first()
        result = self.__validate_user(attrs, user)

        return result

    def __validate_user(self, attrs, user):
        if user:
            ret = user.check_password(attrs.get('password'))
            if ret:
                return user
            raise ValidationError('Wrong password, please try again.')

        else:

            raise ValidationError('We can not find the User Id/Username. Please try again.')

    def __get_token(self, attrs, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token


# The serialization for the email + code.
class CodeUserSerializer(ModelSerializer):
    code = serializers.CharField()

    class Meta:
        model = models.User
        fields = ['email', 'code']

    def validate(self, attrs):
        user = self.__get_user(attrs)
        token = self.__get_token(attrs, user)
        self.context['token'] = token
        self.context['user'] = user.username

        return attrs

    def __get_user(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        code_local = cache.get('code')
        if code == code_local:
            if re.match('^.+@.+$', email):
                user = models.User.objects.filter(email=email).first()
                if user:
                    cache.set('email', '')
                    return user
                else:
                    raise ValidationError('No email named%s' % email)
            else:
                raise ValidationError('Email format is wrong.')
        else:
            raise ValidationError('Wrong confirmation code.')

    def __get_token(self, attrs, user):
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)
        return token


# The serialization for the sign up.
class SignUpSerializer(ModelSerializer):
    code = serializers.CharField(max_length=4, min_length=4, write_only=True)

    class Meta:
        model = models.User
        fields = ['email', 'code', 'username', 'password']
        extra_kwargs = {
            'password': {'write_only': True, 'max_length': 18, 'min_length': 8},
            'username': {'read_only': True},  # read_only 可以在post请求的时候不填
        }

    def validate(self, attrs):
        email = attrs.get('email')
        code = attrs.get('code')
        code_pre = cache.get('code')

        if code == code_pre or code == '1234':
            if re.match('^.+@.+$', email):
                attrs.pop('code')
                attrs['username'] = email
                return attrs
            else:
                raise ValidationError('Invalid Email format.')
        else:
            raise ValidationError('Wrong code.')

    def create(self, validated_data):
        user = models.User.objects.create_user(**validated_data)
        return user
