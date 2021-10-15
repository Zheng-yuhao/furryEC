from django.db import models

class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Create_Time')
    update_time = models.DateTimeField(auto_now=True, verbose_name='Update_Time')
    is_delete = models.BooleanField(default=False, verbose_name='DeleteOrNot')
    is_show = models.BooleanField(default=False, verbose_name='DisplayOrNot')
    display_order = models.IntegerField()

    class Meta:
        abstract = True