from django.urls import path
from rest_framework import routers
from .user import UsersViewSet

router = routers.DefaultRouter()

router.register('api/users', UsersViewSet, 'users')

urlpatterns = router.urls

