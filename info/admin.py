from django.contrib import admin
from .models import infoModel

# Register your models here.
@admin.register(infoModel)
class infoModelAdmin(admin.ModelAdmin):
    list_display = ['topic', 'created', 'updated']


