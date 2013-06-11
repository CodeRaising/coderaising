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
    url(
        r"^skills/(?P<skills>[\w-]+)/$",
        SkillsListView.as_view(),
        name="userprofile_skills_list"
    ),
    url(
        r"^wanttolearn/(?P<learn>[\w-]+)/$",
        LearnListView.as_view(),
        name="userprofile_learn_list"
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
