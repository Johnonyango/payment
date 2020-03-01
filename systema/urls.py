from django.urls import path
from . import views


urlpatterns = [
    path('', views.accessToken, name = 'homepage'),
]
