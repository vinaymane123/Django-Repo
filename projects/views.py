from django.shortcuts import render
from django.http import HttpResponse
from .models import Project
from .forms import ProjectForm

def projects(request):
    projects = Project.objects.all()
    context = {'projects':projects}
    return render(request, 'projects/projects.html', context )


def project(request,pk):
    projectobj = Project.objects.get(id=pk)
   
    return render(request, 'projects/single-project.html',{'project':projectobj })


def createProject(request):
    form = ProjectForm()
    if request.method =='POST':
        print(request.POST)
        #form = ProjectForm(request.POST)
    context = {'form ':form}
    return render(request, "projects/project_form.html", context)
