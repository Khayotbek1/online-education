from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    is_instructor = models.BooleanField(default=False)
    enrolled_courses = models.ManyToManyField('courses.Course', related_name='students', blank=True)

    def __str__(self):
        return self.username

