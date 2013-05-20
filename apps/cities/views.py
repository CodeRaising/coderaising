from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

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

    # def get_context_data(self, **kwargs):
    #     "This is to print your context variables during testing ONLY"
    #     context = super(CitiesListView, self).get_context_data(**kwargs)
    #     print context
    #     return context


class CityDetailView(DetailView):
    """
    Definitely read up on DetailView here:
    http://ccbv.co.uk/projects/Django/1.5/django.views.generic.detail/DetailView/
    This is similar to ListView (context_object_name and all that), but
    here you also need a field to identify the object.
    """
    model = City
    slug_field = "name"
    slug_url_kwarg = "city"


class CohortListView(ListView):
    """
    If I only list the model (like on CitiesListView), it'll show all
    cohorts, but we want to filter by city, so I need to restrict the
    queryset by overriding get_queryset()
    """
    model = Cohort

    def get_queryset(self):
        queryset = super(CohortListView, self).get_queryset()
        city_name = self.kwargs['city']
        return queryset.filter(city__name__exact=city_name)

    def get_context_data(self, **kwargs):
        """
        I wanted to make the template reusable, so it can show
        city cohorts or django cohorts or whatever, so any view that
        renders it just needs to add a "cohort_category" to the context
        """
        context = super(CohortListView, self).get_context_data(**kwargs)
        context['cohort_category'] = self.kwargs['city']
        return context


class CohortDetailView(DetailView):
    # make this work
    pass







####################################
# Old stuff below this line        #
# I'm leaving it in for reference  #
####################################


def functional_dummy_view(request, *args, **kwargs):
    context = {"variable": "it's much better to store logic in views"}
    return render(request, "dummy.html", context)


class ClassyDummyView(TemplateView):
    template_name = "dummy.html"

# That's all that's needed to render the template, but if I want to
# add additional context variables, I can do it like this:

class ClassyDummyView(TemplateView):
    template_name = "dummy.html"

    # override the default functionality of get_context_data
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ClassyDummyView, self).get_context_data(**kwargs)
        # Add in a whatever context you want:
        context['variable'] = "it's much better to store logic in views"
        return context

    # for the default code of TemplateView, see here:
    # http://ccbv.co.uk/projects/Django/1.5/django.views.generic.base/TemplateView/
    # the docs have a description of extending generic views here: 
    # https://docs.djangoproject.com/en/1.5/topics/class-based-views/generic-display/
    
    # I was playing around with other ways to add to the context ('cause that 
    # context['variable'] = 'value' syntax gets tiresome if you have to add a lot
    # of stuff).  Anyways, here are two more ways to do the same thing.  All 3 are fine

    # def get_context_data(self, **kwargs):
    #     # write your context dictionary
    #     context = {'variable': "it's much better to store logic in views"}
    #     # add the **kwargs from the method so you don't mess anything up
    #     context.update(kwargs)
    #     return super(ClassyDummyView, self).get_context_data(**context)

    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(ClassyDummyView, self).get_context_data(**kwargs)
    #     # Add in a whatever context you want:
    #     my_context = {'variable': "it's much better to store logic in views"}
    #     # add yours to the context
    #     context.update(my_context)
    #     return context