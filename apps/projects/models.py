from django.db import models

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
    technologies = models.TextField(default="To be determined, mentor will update")
    cohort = models.ManyToManyField('cities.Cohort', blank=True)
    city = models.ManyToManyField('cities.City', blank=True)
    # is_approved = models.BooleanField(default=False)
    members = models.ManyToManyField(UserProfile, related_name="project_members_set", blank=True)
    mentors = models.ManyToManyField(UserProfile, related_name="project_mentors_set", blank=True)

    def __unicode__(self):
		return self.name

    def save(self, *args, **kwargs):
        # ensure all mentors are members
        return super(Project, self).save(*args, **kwargs)
