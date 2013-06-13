from django.db import models
from taggit.managers import TaggableManager
from apps.userprofile.models import UserProfile
from apps.core_stuff.models import NamedSlugged

class Project(NamedSlugged):
    """
    A team of people working on one project.
    """
    # name = models.CharField(max_length=255)
    description = models.TextField()
    # demo_link = models.URLField(blank=True, null=True)
    # image = models.ImageField()
    technologies = TaggableManager(verbose_name="Technologies", blank=True)
    cohort = models.ManyToManyField('cities.Cohort', blank=True)
    city = models.ManyToManyField('cities.City', blank=True)
    is_approved = models.BooleanField(default=False)
    applicants = models.ManyToManyField(UserProfile, related_name="project_applicants_set", blank=True)
    members = models.ManyToManyField(UserProfile, related_name="project_members_set", blank=True)
    mentors = models.ManyToManyField(UserProfile, related_name="project_mentors_set", blank=True)
    # members = models.ManyToManyField(UserProfile, through="Membership")

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        # ensure all mentors are members
        return super(Project, self).save(*args, **kwargs)

    def has_change_permission(self, request):
        mentor = request.user.userprofile in self.mentors
        if mentor or request.user.is_staff:
            return True

# I'm not doing this for now, I think it's harder to work with
# class Membership(models.Model):
#     """
#     specifies the nature of each person's membership
#     see https://docs.djangoproject.com/en/dev/topics/db/models/#intermediary-manytomany
#     for details on how to use

#     How can we guarantee each user is unique?
#     """
#     user = models.ForeignKey(UserProfile)
#     project = models.ForeignKey(Project)
#     is_accepted = models.BooleanField(default=False)
#     is_mentor = models.BooleanField(default=False)

#     def __unicode__(self):
#         return "%s - %s" % (self.user, self.project)

#     def save(self, *args, **kwargs):
#         # ensure that membership doesn't already exist
#         # and that all mentors are accepted
#         return super(Membership, self).save(*args, **kwargs)