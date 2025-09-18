from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Education(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    school = models.CharField(max_length=200)
    degree = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.degree} at {self.school}"

class WorkExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.position} at {self.company}"

class ProjectExperience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    tech_stack = models.CharField(max_length=200, blank=True)
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.title

class Publication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    year = models.IntegerField()
    link = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.title} ({self.year})"
