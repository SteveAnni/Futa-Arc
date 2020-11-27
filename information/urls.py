from django.urls import path, include
from . import views
urlpatterns = [
    path('info/', views.infomation, name='infomation')
]
