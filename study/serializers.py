from rest_framework import serializers

from study.models import Course, Lesson, Subscription
from study.validators import validate_video_url


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'


class LessonSerializer(serializers.ModelSerializer):
    url = serializers.URLField(validators=[validate_video_url])

    class Meta:
        model = Lesson
        fields = '__all__'


class CourseDetailSerializer(serializers.ModelSerializer):
    count_lessons = serializers.SerializerMethodField()
    lessons = serializers.SerializerMethodField()
    subscription = serializers.SerializerMethodField()

    def get_count_lessons(self, object):
        return object.lesson_set.count()

    def get_lessons(self, object):
        return LessonSerializer(object.lesson_set.all(), many=True).data

    def get_subscription(self, object):
        if self.context.get('request').user.is_authenticated:
            return SubscriptionSerializer(
                Subscription.objects.filter(user=self.context['request'].user, course=object)).exists()

    class Meta:
        model = Course
        fields = ('title', 'description', 'title', 'count_lessons', 'lessons')


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'
