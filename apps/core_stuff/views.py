from django.core.exceptions import PermissionDenied
from django.contrib.auth.views import redirect_to_login

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