from django.db import models

from apps.userprofile.models import UserProfile

class Project(models.Model):
    """
    A team of people working on one project.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    # demo_link = models.URLField(blank=True, null=True)
    # image = models.ImageField()
    technologies = models.TextField(default="To be determined, mentor will update")
    cohort = models.ManyToManyField('cities.Cohort')
    city = models.ManyToManyField('cities.City')
    # is_approved = models.BooleanField(default=False)
    members = models.ManyToManyField(UserProfile, related_name="project_members_set")
    mentors = models.ManyToManyField(UserProfile, related_name="project_mentors_set")

	def __unicode__(self):
		"""
		returns project.name
		"""
		return self.name

    def save(self, *args, **kwargs):
        # ensure all mentors are members
        return super(Project, self).save(*args, **kwargs)
