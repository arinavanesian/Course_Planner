from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from planner.views import CourseViewSet, StudentViewSet
from django.http import HttpResponse

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'students', StudentViewSet)

def home_view(request):
    return HttpResponse("Welcome to the Course Planner API. Use /api/ to access the endpoints.")

urlpatterns = [
    path('', home_view, name='home'),  # Add this line for the root path
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/students/<int:pk>/recommendations/', 
         StudentViewSet.as_view({'get': 'get_recommendations'}), 
         name='student-recommendations'),
]
