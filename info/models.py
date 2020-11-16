from django.db import models

# Create your models here.


class infoModel(models.Model):
    topic = models.CharField(max_length=80)
    info = models.TextField()
    created = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.topic

    class Meta:
        verbose_name_plural = 'Information'

class aggregateList(models.Model):
    username = models.CharField(max_length=50)
    jamb = models.PositiveIntegerField()
    post_utme = models.PositiveIntegerField()
    aggregate = models.PositiveIntegerField()
    created = models.DateField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.username
    class Meta:
        verbose_name_plural = 'Aggregate Table'
    

