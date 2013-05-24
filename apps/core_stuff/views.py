import logging

from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login

logger = logging.getLogger(__name__)

class DebugMixin(object):
    """
    For use in testing out a new view
    """
    def get_context_data(self, **kwargs):
        "This is to print your context variables during testing ONLY"
        context = super(DebugMixin, self).get_context_data(**kwargs)
        print "#########################"
        print "CONTEXT SENT TO TEMPLATE:"
        for k, v in context.items():
            print "  %s: %s" % (k, v)
        print "don't forget to remove this mixin after testing the view"
        print "DON'T FORGET TO REMOVE THIS MIXIN AFTER TESTING THE VIEW"
        print "#########################"        
        return context


class AccessMixin(object):
    """
    'Abstract' mixin that gives access mixins the same customizable
    functionality.
    """
    login_url = settings.LOGIN_URL # LOGIN_URL from project settings
    raise_exception = False # Default whether to raise an exception to none
    redirect_field_name = REDIRECT_FIELD_NAME # Set by django.contrib.auth

    def get_login_url(self):
        """
        Override this method to customize the login_url.
        """
        if self.login_url is None:
            raise ImproperlyConfigured("%(cls)s is missing the login_url. "
                "Define %(cls)s.login_url or override "
                "%(cls)s.get_login_url()." % {"cls": self.__class__.__name__})

        return self.login_url

    def get_redirect_field_name(self):
        """
        Override this method to customize the redirect_field_name.
        """
        if self.redirect_field_name is None:
            raise ImproperlyConfigured("%(cls)s is missing the "
                "redirect_field_name. Define %(cls)s.redirect_field_name or "
                "override %(cls)s.get_redirect_field_name()." % {
                "cls": self.__class__.__name__})

        return self.redirect_field_name


class LoginRequiredMixin(AccessMixin):
    """
    View mixin which verifies that the user is authenticated.

    NOTE:
    This should be the left-most mixin of a view.
    """
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            if self.raise_exception:
                raise PermissionDenied # return a forbidden response
            else:
                return redirect_to_login(
                    request.get_full_path(),
                    self.get_login_url(),
                    self.get_redirect_field_name()
                    )

        return super(LoginRequiredMixin, self).dispatch(request, *args,
            **kwargs)
