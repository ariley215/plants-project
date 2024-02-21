from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Plant
from .seralizer import PlantSerializer
from .permissions import IsOwnerOrReadOnly 

class PlantListView(ListCreateAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = (IsOwnerOrReadOnly,)


class PlantDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer
    permission_classes = (IsOwnerOrReadOnly,)
