from django.db import models

from apps.userprofile.models import UserProfile
from apps.core_stuff.models import NamedSlugged

# City
class City(NamedSlugged):
    # name = models.CharField(max_length=255)
    # slug = models.SlugField()
    description = models.TextField(blank=True)
    organizers = models.ManyToManyField(UserProfile, blank=True)

    def __unicode__(self):
        """
        adding this function to your models lets you define how each
        object appears, rather than "City object", I want the city's
        name
        """
        return self.name


# Cohort
class Cohort(NamedSlugged):
    """
    A class composed of several teams in a given city.
    eg: City: Boston, Cohort: May-2013
    """
    # name = models.CharField(max_length=255)
    # slug = models.SlugField()
    description = models.TextField(blank=True)
    city = models.ForeignKey(City)
    start_date = models.DateField(default=None, blank=True, null=True)
    end_date = models.DateField(default=None, blank=True, null=True)
    members = models.ManyToManyField(
        UserProfile,
        related_name="cohort_members_set",
        blank=True
        )
    organizers = models.ManyToManyField(
        UserProfile,
        related_name="cohort_organizers_set",
        blank=True
        )

    def __unicode__(self):
        """
        I'm including self.city in the unicode representation of this
        object.  That will render according to City()'s __unicode__
        method.  Now in the admin site, the "May 2013" cohort will appear
        in the form "Boston - May 2013"
        """
        return "%s - %s" % (self.city, self.name)