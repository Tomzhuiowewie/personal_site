from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class PortfolioProject(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to="portfolio/")
    link = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
