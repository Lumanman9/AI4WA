from django.urls import path
from .views import CrimeListView

app_name = 'api'
urlpatterns = [
    path('', CrimeListView.as_view(), name='crime_list'),
]
