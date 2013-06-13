from django.conf.urls.defaults import patterns, url
from .views import (
    ProfileListView,
    SkillsListView,
    LearnListView,
    ProfileDetailView,
    ProfileEditView,
    UserEditView
)

urlpatterns = patterns(
    "",
    url(
        r"^$",
        ProfileListView.as_view(),
        name="userprofile_list"
    ),
    # url(
    #     r"^edit/$",
    #     ProfileEditView.as_view(),
    #     name="userprofile_edit"
    # ),
    url(
        r"^edit/$",
        UserEditView.as_view(),
        name="userprofile_edit"
    ),
    url(
        r"^(?P<user>[\w-]+)/$",
        ProfileDetailView.as_view(),
        name="userprofile_detail"
    ),
)
