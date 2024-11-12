from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from study.models import Course, Lesson
from users.models import User


class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='test@example.com')
        self.course = Course.objects.create(title='Тестовый курс', description='Описание')
        self.lesson = Lesson.objects.create(title='Тестовый урок', description='Описание урока', course=self.course,
                                            owner=self.user)
        self.client.force_authenticate(user=self.user)

    def test_lesson_retrieve(self):
        url = reverse('study:lesson-get', args=(self.lesson.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
