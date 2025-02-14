from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('resume', views.resume),
    path('findTeam', views.findTeam),
    path('findMember', views.findMember),
    path('noProfile', views.noProfile)
]