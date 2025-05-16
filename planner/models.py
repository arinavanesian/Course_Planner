from django.db import models

class Course(models.Model):
    CONCENTRATION_CHOICES = [
        ('CORE', 'Core'),
        ('DS', 'Data Science'), 
        ('CS', 'Computer Science'),
        ('ELECTIVE', 'Elective'),
        ('PREP', 'Preparatory')
    ]
    
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    credits = models.PositiveSmallIntegerField()
    concentration = models.CharField(max_length=10, choices=CONCENTRATION_CHOICES)
    description = models.TextField(blank=True)
    difficulty = models.CharField(max_length=10, choices=[
        ('LOW', 'Low'), 
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High')
    ], default='MEDIUM')
    
    def __str__(self):
        return f"{self.code}: {self.name}"

class Prerequisite(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='main_course')
    prerequisite = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='required_for')
    
    class Meta:
        unique_together = ('course', 'prerequisite')

class Student(models.Model):
    name = models.CharField(max_length=100)
    concentration = models.CharField(max_length=10, choices=[
        ('DS', 'Data Science'),
        ('CS', 'Computer Science')
    ])
    completed_courses = models.ManyToManyField(Course, blank=True)
    
    def __str__(self):
        return self.name
