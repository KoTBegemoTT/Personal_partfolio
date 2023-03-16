from django.shortcuts import render, get_object_or_404
from portfolio.models import Project, ProjectImage


def home(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', context={'projects': projects})


def view_project(request, pk):
    project = get_object_or_404(Project, id=pk)
    images = ProjectImage.objects.filter(project=pk)
    return render(request, 'portfolio/view_project.html', context={'project': project, 'images': images})


def test(request):
    return render(request, 'portfolio/test.html')