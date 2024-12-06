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


class CrimeListView(ListView):
    model = Crime
    template_name = 'api/crime_list.html'
    context_object_name = 'crimes'
    ordering = ['-created_at']
    paginate_by = 10  # Optional: adds pagination every 10 items