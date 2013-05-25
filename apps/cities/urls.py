from django.conf.urls.defaults import patterns, include, url
from django.views.generic import TemplateView

from mezzanine.core.views import direct_to_template
from views import calendar
from .views import (
    CitiesListView,
    CityDetailView,
    CohortListView,
    CohortDetailView,
    )

# Note: these views will not work if there's nothing in the database.
# well ListView will show nothing, and DetailView will 404.  
# I added a couple cities to my dev db just for testing.
# Also, the url reversing seems to break if names contain spaces.
# We should add a "slug" field to any model for which we want to use
# the name in urls.  Django has a function that converts arbitrary 
# strings into url-safe strings called slugs.  I'll do this later,
# but for now I don't want us to worry about db migrations.
# anyways, to stay safe while testing, don't have spaces in city
# or cohort names.

urlpatterns = patterns("",
    url(
        r"^$",
        CitiesListView.as_view(),
        name="cities_list"
    ),
    url(
        r"^(?P<city>[\w-]+)/$",
        CityDetailView.as_view(),
        name="city_detail"
    ),
    url (
        r"^(?P<city>[\w-]+)/cohorts/$",
        CohortListView.as_view(),
        name="cohort_list"
    ),
    url(
        r'^(?P<city>[\w-]+)/calendar/$',
        "apps.cities.views.calendar"
    ),
    url(
        r'^(?P<city>[\w-]+)/mentors/$',
        "apps.cities.views.mentors"
    ),
    url(
        r'^(?P<city>[\w-]+)/organizers/$',
        "apps.cities.views.organizers"
    ),
    url(
        r'^(?P<city>[\w-]+)/sponsors/$',
        "apps.cities.views.sponsors"
    ),
    url( # this view has not yet been built
        r"^(?P<city>[\w-]+)/(?P<cohort>[\w-]+)/$",
        CohortDetailView.as_view(),
        name="cohort_detail"
    ),

)