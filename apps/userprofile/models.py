from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField("auth.User", editable=False)
    signup_date = models.DateTimeField("Signup date", auto_now_add = True)
    bio = models.TextField()
    tech_to_learn = models.TextField("Technologies I want to learn more about")
    tech_i_know = models.TextField("Technologies I know")

    def __unicode__(self):
        return self.user.username