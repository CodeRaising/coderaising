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