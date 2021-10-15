from django.db import models
from furryEC.utils.models import BaseModel


# Create your models here.


class Banner(BaseModel):
    name = models.CharField(max_length=32, verbose_name='img_name')
    img = models.ImageField(verbose_name='Carousel img', upload_to='banner',
                            help_text='The size must be 3840*800', null=True)
    link = models.CharField(max_length=32, verbose_name='the Link to another url')
    info = models.TextField(verbose_name='img_description')

    def __str__(self):
        return self.name