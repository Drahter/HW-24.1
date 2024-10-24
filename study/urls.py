from os import path
from rest_framework.routers import DefaultRouter
from study.apps import StudyConfig
from study.views import CourseViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')

app_name = StudyConfig.name

urlpatterns = [] + router.urls
