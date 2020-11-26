from django.contrib import admin
from .models import infoModelClass

# Register your models here.
@admin.register(infoModelClass)
class infoModelClassAdmin(admin.ModelAdmin):
    list_display = ['topic', 'created', 'updated']
  
