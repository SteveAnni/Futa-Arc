from django.urls import path, include
from . import views
urlpatterns = [
    path('auth/register/', views.register_or_login, name='register_or_login'),
    path('auth/current-user/', views.current_user, name='current_user'),
    path('auth/', include('dj_rest_auth.urls'), name='rest_auth')

]
