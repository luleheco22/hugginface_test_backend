from .models import Users
from rest_framework import viewsets, permissions
# from rest_framework.response import Response
# from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework.generics import GenericAPIView
from .serializers import UsersSerializer

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    permission_class = [permissions.AllowAny] 
    serializer_class = UsersSerializer

