from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
    status_code = models.CharField(max_length=5)
    def __str__(self):
        return f"{self.status_code}"

class Course(models.Model):
    course_code = models.CharField(max_length=5)
    course_name = models.CharField(max_length=64)
    course_semester = models.CharField(max_length=1)
    course_year = models.CharField(max_length=5)
    def __str__(self):
        return f"{self.course_code}"
    
class Taking(models.Model):
    status = models.CharField(max_length=5)
    current_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="name")
    seats = models.IntegerField()

    def __str__(self):
        return f"{self.id} {self.current_course} {self.current_course.course_name}"

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    takings = models.ManyToManyField(Taking, blank=True, related_name="students")
    def __str__(self):
        return f"{self.fname} {self.lname}"