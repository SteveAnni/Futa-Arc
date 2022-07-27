from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user_id = models.OneToOneField
    username = models.CharField(max_length=50)
    profile_pic = models.ImageField()
    profile_bio = models.TextField()
    

    def __str__(self):
        return self.username
