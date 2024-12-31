from django.urls import path
from api.views import CrimeListView,CrimeDetailView

app_name = 'crimes'
urlpatterns = [
    path('', CrimeListView.as_view(), name='crime_list'),
    path('<int:pk>/', CrimeDetailView.as_view(), name='crime_detail'),
]
