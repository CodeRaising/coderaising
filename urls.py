from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

from mezzanine.core.views import direct_to_template

from wiki.urls import get_pattern as get_wiki_pattern
from django_notify.urls import get_pattern as get_notify_pattern
from apps.cities.views import ClassyDummyView

admin.autodiscover()

# Add the urlpatterns for any custom Django applications here.
# You can also change the ``home`` view to add your own functionality
# to the project's homepage.

urlpatterns = patterns("",
    url(r"^users/", include("apps.userprofile.urls")),
    url(r"^cities/", include("apps.cities.urls")),

    url(r"^projects/", include("apps.projects.urls")),
    # once we compartmentalize the function into apps (profiles, projects, etc...)
    # it'll make sense to use include() and store the relevant urls within that app
    # Here are four different ways to render a template:

    # dummy1 and dummy2 use only generic views.  They are good for testing new 
    # templates, or for pages that don't need any context variables (say, if 
        # everything will be coded into the html directly).
    # In dummy1, I did add an additional parameter that goes through to the
    # template in the "params" dictionary, but you should generally avoid 
    # this by using an actual view.
    url(
        r"^dummy1/$",
        direct_to_template,
        {"template": "dummy.html", "variable": "You shouldn't put this much in your URLconf"},
        name="dummy1"
        ),
    # this is a better dummy1 implementation (with no additional context passed)
    # url(
    #     r"^dummy1/$",
    #     direct_to_template,
    #     {"template": "dummy.html"},
    #     name="dummy1"
    #     ),
    url(r"^dummy2/$", TemplateView.as_view(template_name="dummy.html"), name="dummy2"),

    # these two examples refer to actual views in apps/core/views.py  For the
    # purposes of just creating a template, it's fine to use one of the two 
    # methods above, but once you start making the template do stuff, you'll
    # want to use a custom view.
    url(r"^dummy3/$", "apps.cities.views.functional_dummy_view", name="dummy3"),
    url(r"^dummy4/$", ClassyDummyView.as_view(), name="dummy4"),


# --------------------------------------------------------------------------
    # preconfigured stuff below this line.

    # Change the admin prefix here to use an alternate URL for the
    # admin interface, which would be marginally more secure.
    url(r"^admin/", include(admin.site.urls)),

    # WIKI URLS
    # ---------
    (r'^wiki/notify/', get_notify_pattern()),
    (r'^wiki/', get_wiki_pattern()),


    # We don't want to presume how your homepage works, so here are a
    # few patterns you can use to set it up.

    # HOMEPAGE AS STATIC TEMPLATE
    # ---------------------------
    # This pattern simply loads the index.html template. It isn't
    # commented out like the others, so it's the default. You only need
    # one homepage pattern, so if you use a different one, comment this
    # one out.

    #url(r"^$", direct_to_template, {"template": "index.html"}, name="home"),

    # HOMEPAGE AS AN EDITABLE PAGE IN THE PAGE TREE
    # ---------------------------------------------
    # This pattern gives us a normal ``Page`` object, so that your
    # homepage can be managed via the page tree in the admin. If you
    # use this pattern, you'll need to create a page in the page tree,
    # and specify its URL (in the Meta Data section) as "/", which
    # is the value used below in the ``{"slug": "/"}`` part.
    # Also note that the normal rule of adding a custom
    # template per page with the template name using the page's slug
    # doesn't apply here, since we can't have a template called
    # "/.html" - so for this case, the template "pages/index.html"
    # should be used if you want to customize the homepage's template.

    url(r"^$", "mezzanine.pages.views.page", {"slug": "/"}, name="home"),

    # HOMEPAGE FOR A BLOG-ONLY SITE
    # -----------------------------
    # This pattern points the homepage to the blog post listing page,
    # and is useful for sites that are primarily blogs. If you use this
    # pattern, you'll also need to set BLOG_SLUG = "" in your
    # ``settings.py`` module, and delete the blog page object from the
    # page tree in the admin if it was installed.

    # url(r"^$", "mezzanine.blog.views.blog_post_list", name="home"),

    # MEZZANINE'S URLS
    # ----------------
    # ADD YOUR OWN URLPATTERNS *ABOVE* THE LINE BELOW.
    # ``mezzanine.urls`` INCLUDES A *CATCH ALL* PATTERN
    # FOR PAGES, SO URLPATTERNS ADDED BELOW ``mezzanine.urls``
    # WILL NEVER BE MATCHED!

    # If you'd like more granular control over the patterns in
    # ``mezzanine.urls``, go right ahead and take the parts you want
    # from it, and use them directly below instead of using
    # ``mezzanine.urls``.
    url(r"^", include("mezzanine_events.urls")),
    url(r"^", include("mezzanine.urls")),

    # MOUNTING MEZZANINE UNDER A PREFIX
    # ---------------------------------
    # You can also mount all of Mezzanine's urlpatterns under a
    # URL prefix if desired. When doing this, you need to define the
    # ``SITE_PREFIX`` setting, which will contain the prefix. Eg:
    # SITE_PREFIX = "my/site/prefix"
    # For convenience, and to avoid repeating the prefix, use the
    # commented out pattern below (commenting out the one above of course)
    # which will make use of the ``SITE_PREFIX`` setting. Make sure to
    # add the import ``from django.conf import settings`` to the top
    # of this file as well.
    # Note that for any of the various homepage patterns above, you'll
    # need to use the ``SITE_PREFIX`` setting as well.

    # url(r"^%s/" % settings.SITE_PREFIX, include("mezzanine.urls"))

)

# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.
handler404 = "mezzanine.core.views.page_not_found"
handler500 = "mezzanine.core.views.server_error"
