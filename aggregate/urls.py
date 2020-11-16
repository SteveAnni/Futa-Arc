from django.urls import path, include
from . import views
urlpatterns = [
    path('add-aggregate-list/', views.aggregate_list, name='aggregate_list'),
    path('get-aggregate-list/', views.get_aggregate_list, name='get_aggregate_list')


]
