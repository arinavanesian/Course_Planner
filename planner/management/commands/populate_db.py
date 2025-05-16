from django.core.management.base import BaseCommand
from planner.models import Course, Prerequisite

class Command(BaseCommand):
    help = 'Populates the database with AUA MS CIS courses'

    def handle(self, *args, **options):
        # Core courses
        cs310 = Course.objects.create(
            code="CS310", 
            name="Theory of Computing",
            credits=3,
            concentration="CORE",
            difficulty="HIGH"
        )
        
        cs340 = Course.objects.create(
            code="CS340",
            name="Machine Learning",
            credits=3,
            concentration="CORE",
            difficulty="HIGH"
        )
        
        # Data Science concentration
        cs346 = Course.objects.create(
            code="CS346",
            name="Artificial Intelligence",
            credits=3,
            concentration="DS",
            difficulty="HIGH"
        )
        
        # Prerequisites
        cs211 = Course.objects.create(
            code="CS211",
            name="Introduction to Algorithms",
            credits=3,
            concentration="PREP",
            difficulty="HIGH"
        )
        
        Prerequisite.objects.create(
            course=cs340,
            prerequisite=cs211
        )
        
        self.stdout.write(self.style.SUCCESS('Database populated with sample courses!'))
