from rest_framework.serializers import ModelSerializer
from . import models


class CourseCategorySerializer(ModelSerializer):
    class Meta:
        model = models.CourseCategory
        fields = ['id', 'name']


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = models.Teacher
        fields = ['id', 'name', 'role_name', 'title', 'signature', 'image', 'brief']


class CourseModelSerializer(ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = models.Course
        fields = [
            'id',
            'name',
            'course_img',
            'brief',
            'level_name',
            'attachment_path',
            'pub_sections',
            'price',
            'students',
            'sections',
            'status_name',
            'teacher',
            'course_type_name',
            'period',
            'section_list',
        ]
