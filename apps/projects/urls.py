from django.conf.urls import patterns, url

from .views import (
		ProjectIndexView,
		ProjectProposeView,
		ProjectDetailView,
		ProjectEditView,
		ProjectUsersView,
		ProjectApplyView,
		ProjectApplicantsView
	)
#from projects import views
#from apps.projects import views

urlpatterns = patterns("",
	# url: /projects/ list view
	url(r"^$", ProjectIndexView.as_view(), name="project_index"),

	#project proposal url: /projects/propose-project
	url(r"^propose_project$", ProjectProposeView.as_view(), name="propose_project"),

	# project details url: /projects/(id)-(slug)/
	url(r"^(?P<pk>\d+)-[\w|\s]+/$", ProjectDetailView.as_view(), name="project_detail"),
	
	# project edit page url: /projects/(id)-(slug)/edit-project
	url(r"^(?P<pk>\d+)-[\w|\s]+/edit-project$", ProjectEditView.as_view(), name="project_edit"),

	# project users list view url: /projects/(id)-(slug)/users
	url(r"^(?P<pk>\d+)-([\w|\s]+)/users$", ProjectUsersView.as_view(), name="project_users"),

	# apply to project url: /projects/(id)-(slug)/apply-to-project
	url(r"^(?P<project_id>\d+)-[\w]+/apply-to-project$", ProjectApplyView.as_view(), name="project_apply"),

	# view applicants url: /projects/(id)-(slug)/view-applicants
	url(r"^(?P<project_id>\d+)-[\w]+/view-applicants$", ProjectApplicantsView.as_view(), name="project_applicants"),

	# project details for /projects/(id)-(slug)/view-applicants/accept-applicants
#url(r"^(?P<project_id>\d+)-[\w]+/view-applicants/accept-applicants$", views.ProjectAcceptApplicantsView.as_view(), name="project_accept_applicants"),
	)

