from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Item
from django.views.generic import ListView, DetailView
from api.models import Crime

from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Sum
from api.serializers import CrimeSerializer
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.authentication import BasicAuthentication



class CrimeListView(ListView):
    model = Crime
    template_name = 'api/crime_list.html'
    context_object_name = 'crimes'
    ordering = ['-created_at']
    paginate_by = 10  # Optional: adds pagination every 10 items

class CrimeDetailView(DetailView):
    model = Crime
    template_name = 'api/crime_detail.html'
    context_object_name = 'crime'

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint for managing users
    """
    @swagger_auto_schema(
        operation_description="Get list of users",
        responses={
            200: 'Success',
            400: 'Bad Request'
        }
    )
    def list(self, request):
        """
        Get a list of all users
        """
        # Your code here
        pass

@swagger_auto_schema(
    operation_description="Protected endpoint requiring authentication",
    security=[{'Bearer': []}, {'Basic': []}],  # Specify security requirements.txt
    responses={
        200: 'Success',
        401: 'Unauthorized',
        403: 'Forbidden'
    }
)
@authentication_classes([JWTAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def protected_view(request):
    # Your view logic here
    pass