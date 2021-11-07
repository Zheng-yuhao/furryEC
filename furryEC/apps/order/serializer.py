from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from django.conf import settings
from . import models
import uuid
from furryEC.libs.alipay import alipay, gateway


class OrderSerializers(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=models.Course.objects.all(),
                                                write_only=True, many=True)

    class Meta:
        model = models.Order
        fields = ['subject',
                  'total_amount',
                  'pay_type',
                  'course', ]

    def _check_price(self, attrs):
        course_list = attrs.get('course')
        total_course_price = attrs.get('total_amount')
        total_order_price = 0
        for course in course_list:
            total_order_price += course.price
        if total_course_price != total_order_price:
            raise ValidationError('The total amount is not compatible')
        return total_order_price

    def _gen_out_trade_no(self):
        return str(uuid.uuid4()).replace('-', '')

    def _get_user(self):
        request = self.context.get('request')
        return request.user

    def _gen_pay_url(self, out_trade_no, total_amount, subject):
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=out_trade_no,
            total_amount=total_amount,
            subject=subject,
            return_url=settings.RETURN_URL,
            notify_url=settings.NOTIFY_URL,
        )
        return gateway + order_string

    def _before_create(self, attrs, user, pay_url, out_trade_no):
        attrs['user'] = user
        attrs['out_trade_no'] = out_trade_no
        self.context['pay_url'] = pay_url

    def validate(self, attrs):
        total_amount = self._check_price(attrs)
        out_trade_no = self._gen_out_trade_no()
        user = self._get_user()
        pay_url = self._gen_pay_url(out_trade_no, total_amount, attrs.get('subject'))
        self._before_create(attrs, user, pay_url, out_trade_no)

        return attrs

    def create(self, validated_data):
        course_list = validated_data.pop('course')
        order = models.Order.objects.create(**validated_data)
        for course in course_list:
            models.OrderDetail.objects.create(order=order,
                                              course=course,
                                              price=course.price,
                                              real_price=course.price)
        return order
