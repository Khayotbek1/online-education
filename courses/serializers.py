from rest_framework import serializers
from .models import *

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'content', 'created_at']
        read_only_fields = ['id', 'created_at']


class CourseSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ('id', 'instructor', 'created_at')

class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'enrolled_at']
        read_only_fields = ['id', 'enrolled_at']

    def validate(self, data):
        user = data['user']
        course = data['course']
        if Enrollment.objects.filter(user=user, course=course).exists():
            raise serializers.ValidationError("Siz bu kursga allaqchon yozilgansiz!")
        return data