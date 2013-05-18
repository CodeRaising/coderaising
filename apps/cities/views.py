from django.shortcuts import render
from django.views.generic import TemplateView

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