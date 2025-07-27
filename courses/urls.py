from django.urls import path
from .views import *


urlpatterns = [
    path('create/', CourseListCreateAPIView.as_view(), name='course-list-create'),
    path('<int:pk>/', CourseRetrieveUpdateDestroyAPIView.as_view(), name='course-detail-update'),
    path('lesson-create/', LessonListCreateAPIView.as_view(), name='lesson-list-create'),
    path('lessons/<int:pk>/', LessonDetailViewAPIView.as_view(), name='lesson-detail-update'),
    path('enroll/', EnrollCourseCreateAPIView.as_view(), name='enroll'),
    path('my-courses/', MyCourseListAPIView.as_view(), name='my-courses'),
]