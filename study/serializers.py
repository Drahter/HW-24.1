from rest_framework import serializers

from study.models import Course, Lesson


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()

    def get_count_lessons(self, object):
        return object.lesson_set.count()

    def get_lessons(self, object):
        return LessonSerializer(object.lesson_set.all(), many=True).data

    class Meta:
        model = Course
        fields = ('title', 'description', 'title', 'count_lessons', 'lessons')
