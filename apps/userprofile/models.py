from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField("auth.User")
    signup_date = models.DateTimeField("Signup date", auto_now_add = True)
    bio = models.TextField()