from django.shortcuts import render
from django.views.generic import (  TemplateView, 
                                    ListView, 
                                    DetailView, 
                                    UpdateView,
                                    CreateView
                                 )
from django.core.urlresolvers import reverse

from apps.userprofile.models import UserProfile
from apps.core_stuff.views import DebugMixin

from .models import Project
from .forms import ProjectForm
from .utils import ProjectPermissions

class ProjectIndexView(ListView):
    model = Project
    template_name="projects/index.html"

class ProjectProposeView(CreateView):
    model = Project
    template_name="projects/propose.html"
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("project_detail",args=(self.object.pk,))


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/detail.html"


class ProjectEditView(ProjectPermissions, UpdateView):
    model = Project
    template_name = "projects/edit.html"
    form_class = ProjectForm
    
    def get_success_url(self):
        a = reverse("project_detail",args=(self.object.pk,))
        return a


###should this be a ListView instead with model = UserProfile???
class ProjectUsersView(DetailView):
    model = Project
    template_name = "projects/users.html"

    def get_queryset(self):
        queryset = super(ProjectUsersView,self).get_queryset()
        return queryset
    
    
### ???
class ProjectApplyView(DetailView):
    model = Project
    slug_field="name"
    slug_url_kwarg = "project"

class ProjectApplicantsView(ListView):
    model = UserProfile
