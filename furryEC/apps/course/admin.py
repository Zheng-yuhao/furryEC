from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Course)
admin.site.register(models.Teacher)
admin.site.register(models.CourseSection)
admin.site.register(models.CourseCategory)
admin.site.register(models.CourseChapter)