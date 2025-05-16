from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Course, Prerequisite, Student
from .serializers import CourseSerializer, StudentSerializer
from .gemini import generate_recommendation
from django.db.models import Q

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_recommendations(self, request, pk=None):
        student = self.get_object()
        
        completed_courses = student.completed_courses.all()
        available = Course.objects.exclude(
            Q(id__in=completed_courses.values_list('id', flat=True)))
        
        def is_available(course):
            prereqs = Prerequisite.objects.filter(course=course)
            return all(p.prerequisite in completed_courses for p in prereqs)
            
        available_courses = [c for c in available if is_available(c)]
        
        recommendations = generate_recommendation(student, available_courses)
        
        return Response({
            'available_courses': CourseSerializer(available_courses, many=True).data,
            'recommendations': recommendations
        })
