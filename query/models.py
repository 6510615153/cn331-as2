from django.db import models

# Create your models here.

class Course(models.Model):
    course_code = models.CharField(max_length=5)
    course_name = models.CharField(max_length=64)
    course_semester = models.CharField(max_length=1)
    course_year = models.CharField(max_length=5)
    def __str__(self):
        return f"{self.course_code}"
    
class Taking(models.Model):
    current_course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="name")
    seats = models.IntegerField()

    def __str__(self):
        return f"{self.current_course} | Available: {self.seats}"

class Student(models.Model):
    fname = models.CharField(max_length=64)
    lname = models.CharField(max_length=64)
    takings = models.ManyToManyField(Taking, blank=True, related_name="students")
    def __str__(self):
        return f"{self.fname} {self.lname}"