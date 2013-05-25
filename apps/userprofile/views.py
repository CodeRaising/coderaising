from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.urlresolvers import reverse

from .models import UserProfile


class ProfileListView(ListView):
    model = UserProfile

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