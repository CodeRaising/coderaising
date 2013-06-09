from django.db import models
from taggit.managers import TaggableManager
from taggit.models import GenericTaggedItemBase, TagBase


class LearnTag(TagBase):
    pass


class LearnTaggedItem(GenericTaggedItemBase):
    tag = models.ForeignKey(LearnTag, related_name="learn")


class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", editable=False)
    signup_date = models.DateTimeField("Signup date", auto_now_add=True)
    bio = models.TextField()
    learn = TaggableManager(verbose_name="Tech I want to learn", through=LearnTaggedItem, blank=True)
    skills = TaggableManager(verbose_name="Tech I know", blank=True)

    def __unicode__(self):
        return self.user.username
