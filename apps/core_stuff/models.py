from django.db import models

from mezzanine.utils.urls import slugify
from mezzanine.utils.models import base_concrete_model

def unique_slug(queryset, slug_field, slug):
    """
    Ensures a slug is unique for the given queryset, appending
    an integer to its end until the slug is unique.
    """
    i = 0
    while True:
        if i > 0:
            if i > 1:
                slug = slug.rsplit("-", 1)[0]
            slug = "%s-%s" % (slug, i)
        try:
            queryset.get(**{slug_field: slug})
        except: # ObjectDoesNotExist:
            break
        i += 1
    return slug

class NamedSlugged(models.Model):
    """
    Abstract parent model that provides a name field and an
    auto-generated slug field
    """
    name = models.CharField(max_length=500)
    slug = models.CharField(max_length=2000, blank=True, null=True,
        help_text="Leave blank to have the URL auto-generated from the name")

    class Meta:
        abstract = True

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        """
        Create a unique slug by appending an index.
        """
        if not self.slug:
            self.slug = self.get_slug()
        concrete_model = base_concrete_model(NamedSlugged, self)
        slug_qs = concrete_model.objects.exclude(id=self.id)
        self.slug = unique_slug(slug_qs, "slug", self.slug)
        super(NamedSlugged, self).save(*args, **kwargs)

    def get_slug(self):
        """
        Allows subclasses to implement their own slug creation logic.
        """
        return slugify(self.name)

    def admin_link(self):
        return "<a href='%s'>%s</a>" % (self.get_absolute_url(),
                                        ugettext("View on site"))
    admin_link.allow_tags = True
    admin_link.short_description = ""

