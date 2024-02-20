from django.urls import path
from .views import PlantListView, PlantDetailView

urlpatterns = [
  path('', PlantListView.as_view(), name="plant_list"),
  path('<int:pk>/', PlantDetailView.as_view(), name='plant_detail'),
]