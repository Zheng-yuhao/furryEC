from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from furryEC.utils import response

from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from . import models
from . import serialize
from django.conf import settings

# Create your views here.


class BannerView(ListModelMixin, GenericViewSet):
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('display_order')[:settings.BANNER_COUNTER]
    serializer_class = serialize.BannerModelSerializer
