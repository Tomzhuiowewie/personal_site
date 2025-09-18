from django.contrib import admin
from .models import Education, WorkExperience, ProjectExperience, Publication

admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(ProjectExperience)
admin.site.register(Publication)
