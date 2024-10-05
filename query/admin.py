from django.contrib import admin

from .models import Course, Taking, Student

# Register your models here.

class TakingAdmin(admin.ModelAdmin):
    list_display = ("current_course", "seats")

class StudentAdmin(admin.ModelAdmin):
    filter_horizontal = ("takings", )

admin.site.register(Course)
admin.site.register(Taking, TakingAdmin)
admin.site.register(Student, StudentAdmin)