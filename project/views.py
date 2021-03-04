from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Project

# Create your views here.
class ProjectList(ListView):
    model = Project
    template_name = 'project/project_list.html'
    paginate_by = 5 # 한 페이지에 보여줄 오브젝트 갯수
    context_object_name = 'project_list'

    
class ProjectDetail(DetailView):
    model = Project
    template_name = 'project/project_detail.html'
    context_object_name = 'project'
    
    
