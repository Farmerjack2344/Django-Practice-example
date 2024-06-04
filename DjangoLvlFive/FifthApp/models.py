from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class UserProfileInfo(models.Model):
    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)# Means that this field is required to be filled
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        # Built-in attribute
        # diango.contrib.auth.models.User
        return self.user.username



# This new model makes an extension on the pre existing models
