from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from furryEC.utils import response
from django.core.cache import cache

from rest_framework.mixins import ListModelMixin
from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from . import models
from . import serialize
from django.conf import settings
from rest_framework.response import Response


# Create your views here.


class BannerView(ListModelMixin, GenericViewSet):
    queryset = models.Banner.objects.filter(is_delete=False, is_show=True).order_by('orders')[
               :settings.BANNER_COUNTER]
    serializer_class = serialize.BannerModelSerializer

    def list(self, request, *args, **kwargs):
        if not cache.get('banner_list'):
            res = super().list(request, *args, **kwargs)
            cache.set('banner_list', res.data, 60 * 60 * 24)
            return res
        banner_list = cache.get('banner_list')
        return Response(data=banner_list)
