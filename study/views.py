from rest_framework import viewsets

from study.models import Course
from study.serializers import CourseSerializer


class CourseViewSet(viewsets.ViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
