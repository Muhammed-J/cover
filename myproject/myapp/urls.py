from django.urls import path
from . import views

urlpatterns = [
    path('', views.front_cover, name='front_cover'),
]
