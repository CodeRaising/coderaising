from django.db import models


# City
class City(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    organizers = models.ManyToManyField("UserProfile")


# Cohort
class Cohort(models.Model):
    """
    A class composed of several teams in a given city.
    eg: City: Boston, Cohort: May-2013
    """
    name = models.CharField(max_length=255)
    description = models.TextField()
    city = models.ForeignKey(City)
    start_date = models.DateField()
    end_date = models.DateField()
    members = models.ManyToManyField("UserProfile")
    organizers = models.ManyToManyField("UserProfile")


# Project
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


# UserProfile
class UserProfile(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    tech_to_learn = models.TextField("Technologies I want to learn more about")
    tech_i_know = models.TextField("Technologies I know")
    # default value for description (that includes template)
