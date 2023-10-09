from django.urls import path
from . import views

urlpatterns = [
    path('/emotions', views.getDataEmotions),
    path('/sentiments', views.getDataSentiment)
]

