from django.shortcuts import render
from .models import Project
# Create your views here.


def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects':projects})
