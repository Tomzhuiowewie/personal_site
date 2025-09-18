from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from apps.accounts.models import CustomUser
from apps.resume.models import Education, WorkExperience, ProjectExperience, Publication
from apps.blog.models import BlogPost
from apps.portfolio.models import PortfolioProject
from django.utils import timezone
import random

User = get_user_model()

class Command(BaseCommand):
    help = 'Populates the database with sample data'

    def handle(self, *args, **options):
        self.stdout.write("Creating sample data...")
        
        # Create admin user
        admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            bio='Site administrator'
        )
        
        # Create sample education
        educations = [
            {
                'school': 'Tech University',
                'degree': 'Bachelor of Computer Science',
                'start_date': '2015-09-01',
                'end_date': '2019-06-30'
            },
            {
                'school': 'Coding Bootcamp',
                'degree': 'Full Stack Web Development',
                'start_date': '2020-01-15',
                'end_date': '2020-07-15'
            }
        ]
        
        for edu in educations:
            Education.objects.create(user=admin, **edu)
        
        # Create sample work experience
        jobs = [
            {
                'company': 'Tech Solutions Inc.',
                'position': 'Senior Software Engineer',
                'description': 'Developed web applications using Django and React',
                'start_date': '2020-08-01',
                'end_date': None
            },
            {
                'company': 'Digital Agency',
                'position': 'Web Developer',
                'description': 'Built client websites and e-commerce solutions',
                'start_date': '2019-07-01',
                'end_date': '2020-07-31'
            }
        ]
        
        for job in jobs:
            WorkExperience.objects.create(user=admin, **job)
        
        # Create sample projects
        projects = [
            {
                'title': 'E-commerce Platform',
                'description': 'Built a full-featured online store with payment integration',
                'tech_stack': 'Django, React, PostgreSQL, Stripe',
                'link': 'https://example.com/shop'
            },
            {
                'title': 'Task Management App',
                'description': 'Developed a productivity application with team collaboration',
                'tech_stack': 'Node.js, MongoDB, Vue.js',
                'link': 'https://example.com/tasks'
            }
        ]
        
        for proj in projects:
            ProjectExperience.objects.create(user=admin, **proj)
        
        # Create sample publications
        publications = [
            {
                'title': 'Modern Web Development Practices',
                'journal': 'Tech Journal',
                'year': 2022,
                'link': 'https://example.com/article1'
            }
        ]
        
        for pub in publications:
            Publication.objects.create(user=admin, **pub)
        
        # Create sample blog posts
        blog_posts = [
            {
                'title': 'Getting Started with Django',
                'content': 'Django is a powerful web framework for Python...',
                'tags': 'django, python, webdev'
            },
            {
                'title': 'React Hooks Explained',
                'content': 'Hooks allow you to use state and other React features...',
                'tags': 'react, javascript, frontend'
            }
        ]
        
        for post in blog_posts:
            BlogPost.objects.create(author=admin, **post)
        
        # Create sample portfolio projects
        portfolio_projects = [
            {
                'name': 'E-commerce Website',
                'description': 'A fully responsive online store with payment processing',
                'link': 'https://example.com/store',
                'github': 'https://github.com/example/store'
            },
            {
                'name': 'Mobile Fitness App',
                'description': 'Cross-platform fitness tracking application',
                'link': 'https://example.com/fitness',
                'github': 'https://github.com/example/fitness'
            }
        ]
        
        for proj in portfolio_projects:
            PortfolioProject.objects.create(**proj)
        
        self.stdout.write(self.style.SUCCESS('Successfully populated database with sample data'))
