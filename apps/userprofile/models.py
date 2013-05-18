from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    signup_date = models.DateTimeField("Signup date", auto_now_add = True)
    bio = models.TextField()
    tech_to_learn = models.TextField("Technologies I want to learn more about")
    tech_i_know = models.TextField("Technologies I know")