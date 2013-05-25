from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

from mezzanine.core.views import direct_to_template

from .views import (
    ProfileListView,
    ProfileDetailView,
    ProfileEditView,
    )

urlpatterns = patterns("",
    url(
        r"^$",
        ProfileListView.as_view(),
        name="userprofile_list"
    ),
    url(
        r"^edit/$",
        ProfileEditView.as_view(),
        name="userprofile_edit"
    ),
    url(
        r"^(?P<user>[\w-]+)/$",
        ProfileDetailView.as_view(),
        name="userprofile_detail"
    ),
)