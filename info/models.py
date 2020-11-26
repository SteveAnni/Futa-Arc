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


