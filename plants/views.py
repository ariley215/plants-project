from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Plant
from .seralizer import PlantSerializer

class PlantListView(ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


class PlantDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
