from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class aggregateList(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    jamb = models.PositiveIntegerField()
    post_utme = models.PositiveIntegerField()
    aggregate = models.PositiveIntegerField()
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.username.username
    class Meta:
        verbose_name_plural = 'Aggregate Table'
    

