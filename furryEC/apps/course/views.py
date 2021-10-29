from django.shortcuts import render
from rest_framework.filters import OrderingFilter, SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from . import models
from . import serializer
from .pagnation import CoursePagination


# category view
class CourseCategoryView(GenericViewSet, ListModelMixin):
    queryset = models.CourseCategory.objects.filter(is_delete=False, is_show=True).order_by('orders')
    serializer_class = serializer.CourseCategorySerializer


# Course API
class CourseView(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = models.Course.objects.filter(is_delete=False, is_show=True).order_by('orders')
    print(queryset)
    serializer_class = serializer.CourseModelSerializer
    pagination_class = CoursePagination
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ['id', 'price', 'students']

    filter_fields = ['course_category']

