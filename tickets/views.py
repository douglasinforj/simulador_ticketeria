from django.shortcuts import render

from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators  import action
from .models import Cliente, Evento, Ingresso
from .serializers import ClienteSerializer, EventoSerializer, IngressoSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer

class IngressoViewSet(viewsets.ModelViewSet):
    queryset = Ingresso.objects.all()
    serializer_class = IngressoSerializer

    @action(detail=False, methods=['get'])
    def vendidos(self, request):
        # EndPoint pública
        ingresso = Ingresso.objects.all()
        serializer = IngressoSerializer(ingresso, many=True)
        return Response(serializer.data)

