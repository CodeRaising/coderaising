from django.db import models

class Project(models.Model):
    """
    A team of people working on one project.
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    # demo_link = models.URLField(blank=True, null=True)
    # image = models.ImageField()
    technologies = models.TextField(default="To be determined, mentor will update")
    cohort = models.ManyToManyField(Cohort)
    city = models.ManyToManyField(City)
    # is_approved = models.BooleanField(default=False)
    members = models.ManyToManyField("UserProfile")
    mentors = models.ManyToManyField("UserProfile")

    def save(self, *args, **kwargs):
        # ensure all mentors are members
        return super(Project, self).save(*args, **kwargs)