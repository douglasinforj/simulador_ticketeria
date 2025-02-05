from rest_framework import serializers
from .models import Cliente, Evento, Ingresso


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class EventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = '__all__'

class IngressoSerializer(serializers.ModelSerializer):

    cpf = serializers.CharField(write_only=True)           #Recebendo cpf na requisição
    evento_id = serializers.IntegerField(write_only=True)  #Recebendo o evento

    cliente_nome = serializers.CharField(source="cliente.nome", read_only=True)  # Retorna o nome do cliente
    cliente_cpf = serializers.CharField(source="cliente.cpf", read_only=True)  # Retorna o CPF do cliente
 
    class Meta:
        model = Ingresso
        fields = ['cpf', 'evento_id', 'codigo_ingresso', 'codigo_barras', 'cliente_nome', 'cliente_cpf']  # Mostra apenas esses campos na resposta
        read_only_fields = ['codigo_ingresso', 'codigo_barras', 'cliente_nome', 'cliente_cpf']  # Gera automaticamente


    def create(self, validated_data):
        #buscar o cliente pelo cpf
        cpf = validated_data.pop('cpf')
        evento_id = validated_data.pop('evento_id')

        try:
            cliente = Cliente.objects.get(cpf=cpf)
        except Cliente.DoesNotExist:
            raise serializers.ValidationError({"cpf": "Cliente com este CPF não encontrado."})
        
        try:
            evento = Evento.objects.get(id=evento_id)
        except Evento.DoesNotExist:
            raise serializers.ValidationError({"evento_id": "Evento não encontrado."})
        
        # Criar o ingresso com cliente e evento encontrados
        ingresso = Ingresso.objects.create(cliente=cliente, evento=evento, **validated_data)
        return ingresso