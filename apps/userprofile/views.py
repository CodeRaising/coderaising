from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView, ListView, DetailView, UpdateView, FormView
from django.http import HttpResponseRedirect

from braces.views import LoginRequiredMixin

from .models import UserProfile
from .forms import UserForm, UserProfileForm


class ProfileListView(ListView):
    model = UserProfile

    def get_queryset(self):
        profiles = super(ProfileListView, self).get_queryset()
        filters = self.request.GET
        if "learn" in filters:
            profiles = profiles.filter(learn__name__in=[filters["learn"]])
        if "skills" in filters:
            profiles = profiles.filter(skills__name__in=[filters["skills"]])
        return profiles


class SkillsListView(ProfileListView):
    context_object_name = 'userprofile_list'

    def get_queryset(self):
        return UserProfile.objects.filter(skills__name__in=[self.kwargs['skills']]).distinct()


class LearnListView(ProfileListView):
    context_object_name = 'userprofile_list'

    def get_queryset(self):
        return UserProfile.objects.filter(learn__name__in=[self.kwargs['learn']]).distinct()


class ProfileDetailView(DetailView):
    model = UserProfile
    pk_url_kwarg = 'user'


class ProfileEditView(UpdateView):
    model = UserProfile

    def get_success_url(self):
        return reverse('userprofile_detail', args=(self.object.pk,))

    def get_object(self, queryset=None):
        return self.request.user.userprofile

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(ProfileEditView, self).dispatch(*args, **kwargs)


class UserEditView(LoginRequiredMixin, FormView):
    template_name = "userprofile/edit_user.html"

    def get_form_kwargs(self, obj):
        kwargs = {'instance': obj}
        if self.request.method in ('POST', 'PUT'):
            kwargs.update({
            'data': self.request.POST,
            'files': self.request.FILES,
            })
        return kwargs

    def get_user_forms(self):
        self.user_form = UserForm(
            **self.get_form_kwargs(self.request.user)
        )
        self.userprofile_form = UserProfileForm(
            **self.get_form_kwargs(self.request.user.userprofile)
        )

    def render_forms(self):
        context = self.get_context_data(
            user_form=self.user_form,
            userprofile_form=self.userprofile_form
        )
        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        self.get_user_forms()
        return self.render_forms()

    def post(self, request, *args, **kwargs):
        self.get_user_forms()
        if self.user_form.is_valid() and self.userprofile_form.is_valid():
            self.user_form.save()
            self.userprofile_form.save()
            url = reverse( 'userprofile_detail', args=(self.request.user.userprofile.pk,) )
            return HttpResponseRedirect(url)
        else:
            return self.render_forms()
