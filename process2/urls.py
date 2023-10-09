from django.urls import path
from .views import MyClass

urlpatterns = [
    path('', MyClass.as_view()),
]
