from rest_framework import serializers

from study.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()

    def get_count_lessons(self, object):
        return object.lesson_set.count()

    class Meta:
        model = Course
        fields = ('title', 'description', 'title', 'count_lessons')


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
