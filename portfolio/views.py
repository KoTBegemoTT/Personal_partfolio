from django.shortcuts import render, get_object_or_404
from portfolio.models import Project


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', context={'projects': projects})


def view_project(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/view_project.html', context={'project': project})
