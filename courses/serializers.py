from rest_framework import serializers
from .models import *


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'course', 'title', 'content', 'created_at']


class LessonForCreateCourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'content']


class CourseCreateSerializer(serializers.ModelSerializer):
    lessons = LessonForCreateCourseSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'lessons' ]

    def create(self, validated_data):
        user = self.context['request'].user
        lessons = validated_data.pop('lessons')
        course = Course.objects.create(
            instructor=user,
            title=validated_data['title'],
            description=validated_data['description'],
            price=validated_data['price'],
        )

        for lesson in lessons:
            Lesson.objects.create(
                course=course,
                title=lesson['title'],
                content=lesson['content'],
            )
        return course


class LessonForCourseUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = "__all__"



class CourseUpdateSerializer(serializers.ModelSerializer):
    lessons = LessonForCourseUpdateSerializer(many=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'price', 'lessons' ]

    def update(self, instance, validated_data):
        lessons_data = validated_data.pop('lessons', [])


        for lesson in lessons_data:
            lesson_id = lesson.get('id')
            print(lesson_id)
            if lesson_id:
                Lesson.objects.filter(id=lesson_id, course=instance).update(
                    title=lesson.get('title', ''),
                    content=lesson.get('content', ''),
                )

        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.price = validated_data.get('price', instance.price)
        instance.save()

        return instance


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
