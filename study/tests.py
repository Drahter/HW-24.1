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
        self.assertEqual(
            data.get('title'), 'Тестовый урок'
        )

    def test_lesson_create(self):
        url = reverse('study:lesson-create')
        data = {
            'title': 'Новый урок',
            'description': 'Описание нового урока',
            'course': self.course.pk,
            'url': 'http://youtube.com/watch?v=123'
        }
        response = self.client.post(url, data)
        self.assertEqual(
            response.status_code, status.HTTP_201_CREATED
        )
        self.assertEqual(
            Lesson.objects.all().count(), 2
        )

    def test_lesson_update(self):
        url = reverse('study:lesson-update', args=(self.lesson.pk,))
        data = {
            'title': 'Измененный урок',
            'description': 'Описание измененного урока',
            'course': self.course.pk,
            'url': 'http://youtube.com/watch?v=1234'
        }
        response = self.client.patch(url, data)
        data = response.json()
        self.assertEqual(
            response.status_code, status.HTTP_200_OK
        )
        self.assertEqual(
            data.get('title'), 'Измененный урок'
        )
        self.assertEqual(
            data.get('description'), 'Описание измененного урока'
        )

    def test_lesson_delete(self):
        url = reverse('study:lesson-delete', args=(self.lesson.pk,))
        response = self.client.delete(url)
        self.assertEqual(
            response.status_code, status.HTTP_204_NO_CONTENT
        )
        self.assertEqual(
            Lesson.objects.all().count(), 0
        )
