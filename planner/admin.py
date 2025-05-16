from django.contrib import admin
# planner/admin.py
from .models import Student, Course, Prerequisite

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Prerequisite)
