from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from apps.core_stuff.views import DebugMixin
from .models import City, Cohort

class CitiesListView(ListView):
    """
    Definitely read up on ListView here:
    http://ccbv.co.uk/projects/Django/1.5/django.views.generic.list/ListView/
    By default it'll show all objects that match the model
    you reference.  get_context_data will define two context variables
    that point to this queryset, "object_list" and another one that's
    either <lowercase_model_name>_list (as defined in get_context_object_name)
    or context_object_name if you define it in the class attributes
    """
    model = City
    # ListView generates a template name from the model, so I don't
    # need to define it here.
    # template_name="cities/city_list.html"
    # context_object_name = variable_to_use_in_templates


class CityDetailView(DetailView):
    """
    Definitely read up on DetailView here:
    http://ccbv.co.uk/projects/Django/1.5/django.views.generic.detail/DetailView/
    This is similar to ListView (context_object_name and all that), but
    here you also need a field to identify the object.
    """
    model = City
    # slug_field = "name"
    slug_url_kwarg = "city"


class CohortListView(ListView):
    """
    If I only list the model (like on CitiesListView), it'll show all
    cohorts, but we want to filter by city, so I need to restrict the
    queryset by overriding get_queryset().
    """
    model = Cohort

    def get_queryset(self):
        # get the city object
        slug = self.kwargs.get("city", None)
        self.city = City.objects.get(slug=slug)
        # get the unfiltered queryset (which returns ALL cohorts)
        queryset = super(CohortListView, self).get_queryset()
        # filter by city
        return queryset.filter(city=self.city)

    def get_context_data(self, **kwargs):
        """
        I wanted to make the template reusable, so it can show
        city cohorts or django cohorts or whatever, so any view that
        renders it just needs to add a "cohort_category" to the context
        """
        context = super(CohortListView, self).get_context_data(**kwargs)
        # get_queryset adds a city attribute to the class, which
        # we can use here to get the city name
        context['cohort_category'] = self.city.name
        context['city'] = self.city.name
        return context


class CohortDetailView(DetailView):
    # make this work
    # pass
    model = Cohort
    slug_url_kwarg = "cohort"
    def get_context_data(self, **kwargs):
        context = super(CohortDetailView, self).get_context_data(**kwargs)
        slug = self.kwargs.get("city", None)
        self.city = City.objects.get(slug=slug)
        context['city'] = self.city.name
        return context
#     ProjectListView
#
# class ProjectListView(ListView):
#     model = Project
#
#     def get_queryset(self):
#         slug = self.kwargs.get("cohort", None)
#         self.cohort = Cohort.objects.get(slug=slug)
#         queryset = super(ProjectListView, self).get_queryset()
#         return queryset.filter(cohort=self.cohort)
#
#     def get_context_data(self, **kwargs):
#         context = super(ProjectListView, self).get_context_data(**kwargs)
#         context['cohort'] = self.cohort.name
#         return context


def calendar(request,**kwargs):
    # city = "Boston"
    for key in kwargs:
        city = kwargs.get(key).capitalize()
    return render(request, 'cities/calendar.html', {'city': city})

def mentors(request,**kwargs):
    # city = "Boston"
    for key in kwargs:
        city = kwargs.get(key).capitalize()
    return render(request, 'cities/mentors.html', {'city': city})

def organizers(request,**kwargs):
    # city = "Boston"
    for key in kwargs:
        city = kwargs.get(key).capitalize()
    return render(request, 'cities/organizers.html', {'city': city})

def sponsors(request,**kwargs):
    # city = "Boston"
    for key in kwargs:
        city = kwargs.get(key).capitalize()
    return render(request, 'cities/sponsors.html', {'city': city})
