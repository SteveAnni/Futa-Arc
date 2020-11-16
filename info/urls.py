from django.urls import path, include
from . import views
urlpatterns = [
    path('info/', views.infomation, name='infomation'),
    path('aggregate-list/', views.aggregate_list, name='aggregate_list'),


]
