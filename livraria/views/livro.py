from django.shortcuts import render

from rest_framework.viewsets import ModelViewSet

from livraria.models import Livros

from livraria.serializers import LivrosSerializer, LivrosDetailSerializer, LivrosListSerializer
  
class LivrosViewSet(ModelViewSet):
    queryset = Livros.objects.all()
    serializer_class = LivrosSerializer

    serializer_classes = {
        "list": LivrosListSerializer,
        "retrieve": LivrosDetailSerializer,
    }

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, LivrosSerializer)