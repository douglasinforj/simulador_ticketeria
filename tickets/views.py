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
        """Lista todos os ingressos vendidos, incluindo o CPF do comprador"""
        ingressos = Ingresso.objects.all()
        serializer = IngressoSerializer(ingressos, many=True)
        return Response(serializer.data)



    def create(self, request, *args, **kwargs):
        
        """Cria um ingresso a partir do CPF e do evento"""

        cpf = request.data.get("cpf")
        evento_id = request.data.get("evento_id")

        if not cpf or not evento_id:
            return Response({"erro": "CPF e evento_id são obrigatórios."}, status=status.HTTP_400_BAD_REQUEST)

        # Buscar o cliente pelo CPF
        try:
            cliente = Cliente.objects.get(cpf=cpf)
        except Cliente.DoesNotExist:
            return Response({"erro": "Cliente não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Buscar o evento pelo ID
        try:
            evento = Evento.objects.get(id=evento_id)
        except Evento.DoesNotExist:
            return Response({"erro": "Evento não encontrado."}, status=status.HTTP_404_NOT_FOUND)

        # Criar ingresso
        ingresso = Ingresso.objects.create(cliente=cliente, evento=evento)
        serializer = IngressoSerializer(ingresso)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
