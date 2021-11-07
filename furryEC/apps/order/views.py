from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from . import models
from .serializer import OrderSerializers
from rest_framework.response import Response

class PayView(GenericViewSet, CreateModelMixin):
    queryset = models.Order.objects.all()
    serializer_class = OrderSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(data=serializer.context.get('pay_url'))