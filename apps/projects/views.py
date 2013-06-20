from django.http import HttpResponseRedirect
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
)
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from apps.userprofile.models import UserProfile
from .models import Project
from .forms import ProjectForm
from .utils import ProjectPermissions


class ProjectIndexView(ProjectPermissions, ListView):
    model = Project
    template_name = "projects/index.html"

    def get_queryset(self):
        projects = super(ProjectIndexView, self).get_queryset()
        filters = self.request.GET
        if "tech" in filters:
            projects = projects.filter(technologies__name__in=[filters["tech"]]).distinct()
        return projects


class ProjectProposeView(LoginRequiredMixin, CreateView):
    model = Project
    template_name = "projects/propose.html"
    form_class = ProjectForm

    def get_success_url(self):
        obj = self.object
        return reverse("project_detail", args=(obj.pk,obj.slug))


class ProjectDetailView(DetailView):
    model = Project
    template_name = "projects/detail.html"

    def post(self, request, *args, **kwargs):
        proj = self.get_object()
        if not request.user.is_authenticated():
       		#redirects to project detail page after signin, user needs to click apply button again
            #should user application be automatically be taken care of after successful login???
            url = "/accounts/login?next=" + reverse("project_detail", args=(proj.pk, proj.slug))
            return HttpResponseRedirect(url)
        else:
            if request.user.userprofile not in proj.applicants.all():
                proj.applicants.add(request.user.userprofile)
                #proj.save() #is this needed???
            return HttpResponseRedirect(reverse("project_detail", args=(proj.pk, proj.slug)))


class ProjectEditView(ProjectPermissions, UpdateView):
    model = Project
    template_name = "projects/edit.html"
    form_class = ProjectForm

    def get_success_url(self):
        return reverse("project_detail", args=(self.object.pk,))


class ProjectApplicants(ProjectPermissions, DetailView):
    """
    Lets project mentors and site staff view and approve applicants
    to a project.  Currently this list is sorted by userprofile pk;
    we need to use a "through" field to store "datetime applied" on
    the relationship to sort by the order in which applicants applied.
    """
    template_name = "projects/applicants.html"
    model = Project

    def post(self, request, *args, **kwargs):
        project = self.get_object()
        accepted = request.POST.getlist("applicants")
        if accepted:
            for pk in accepted:
                applicant = UserProfile.objects.get(pk=pk)
                # remove from applicants list
                project.applicants.remove(applicant)
                # add to members list
                project.members.add(applicant)
        return HttpResponseRedirect(reverse("project_detail", args=(project.pk, project.slug)))


###should this be a ListView instead with model = UserProfile???
class ProjectUsersView(DetailView):
    model = Project
    template_name = "projects/users.html"

    def get_queryset(self):
        queryset = super(ProjectUsersView, self).get_queryset()
        return queryset


### ???
class ProjectApplyView(DetailView):
    model = Project
    slug_field = "name"
    slug_url_kwarg = "project"


class ProjectApplicantsView(ListView):
    model = UserProfile
