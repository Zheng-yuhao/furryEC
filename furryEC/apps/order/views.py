from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet
from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . import models
from .serializer import OrderSerializers
from rest_framework.response import Response
from furryEC.libs.alipay import alipay
from furryEC.utils.logger import log


class PayView(GenericViewSet, CreateModelMixin):
    authentication_classes = [JSONWebTokenAuthentication, ]
    permission_classes = [IsAuthenticated, ]
    queryset = models.Order.objects.all()
    serializer_class = OrderSerializers

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(data=serializer.context.get('pay_url'))


class SuccessView(APIView):
    def get(self, request, *args, **kwargs):
        out_trade_no = request.query_params.get('out_trade_no')
        order = models.Order.objects.filter(out_trade_no=out_trade_no).first()
        if order.order_status == 1:
            return Response(True)
        else:
            return Response(False)

    def post(self, request, *args, **kwargs):
        data = request.data
        out_trade_no = data.get('out_trade_no', None)
        gmt_payment = data.get('gmt_payment', None)
        signature = data.pop("sign")
        success = alipay.verify(data, signature)
        if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
            log.info('%s:order success'%out_trade_no)
            return Response('success')
        else:
            log.error('%s:order has error'%out_trade_no)
            return Response('error')
