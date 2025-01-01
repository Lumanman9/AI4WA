from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from core.serializers import HasuraTokenObtainPairSerializer
# Create your views here.
class HasuraTokenObtainPairView(TokenObtainPairView):
    serializer_class = HasuraTokenObtainPairSerializer