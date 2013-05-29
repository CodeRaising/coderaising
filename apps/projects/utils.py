from django.core.exceptions import PermissionDenied


class ProjectPermissions(object):
    """
    Blocks access to a view.  Default implementation only allows
    project mentors access to the view.  To allow any accepted
    members, set permission_required = "member" in your view
    """
    permission_required = "mentor"

    def get_object(self, queryset=None):
        project = super(ProjectPermissions, self).get_object(queryset=None)
        is_mentor = self.request.user.userprofile in project.mentors.all()
        if is_mentor or self.request.user.is_staff:
            return project
        elif self.permission_required == "member":
            if self.request.user.userprofile in project.members.all():
                return project
        raise PermissionDenied