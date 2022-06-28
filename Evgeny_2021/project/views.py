from .models import Project
from django.shortcuts import render


def project_index(request):
    projects = Project.objects.all()
    context = {
        'project': projects
    }
    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)
