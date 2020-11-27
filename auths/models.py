from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.CharField(max_length=290)
    password = models.CharField(max_length=80, editable=False)
    confirm_password = models.CharField(max_length=50, editable=False)

    def __str__(self):
        return self.username.username
