from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import  Project


class IndexView(ListView):
    template_name = 'main/index.html'
    context_object_name = 'all_projects_list'

    def get_queryset(self):
        return Project.objects.all()


class ProjectDetailView(DetailView):
    template_name = 'main/detail.html'
    #model = Project

