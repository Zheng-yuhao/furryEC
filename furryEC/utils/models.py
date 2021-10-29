from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='Create_Time')
    updated_time = models.DateTimeField(auto_now=True, verbose_name='Update_Time')
    is_delete = models.BooleanField(default=False, verbose_name='DeleteOrNot')
    is_show = models.BooleanField(default=False, verbose_name='DisplayOrNot')
    orders = models.IntegerField()

    class Meta:
        abstract = True
