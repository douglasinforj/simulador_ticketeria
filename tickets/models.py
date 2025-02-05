from django.db import models

import uuid
import barcode
from barcode.writer import ImageWriter

import os
from django.conf import settings


class Cliente(models.Model):
    nome = models.CharField(max_length=255)
    cpf= models.CharField(max_length=14, unique=True)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome

class Evento(models.Model):
    nome = models.CharField(max_length=255)
    data = models.DateTimeField()
    local = models.CharField(max_length=255)

    def __str__(self):
        return self.nome
    

class Ingresso(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE)
    codigo_ingresso = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    codigo_barras = models.ImageField(upload_to='barcodes/', blank=True, null=True)

    def save(self, *args, **kwargs):

        #Garantia a pasta exista
        pasta_barcodes = os.path.join(settings.MEDIA_ROOT, 'barcode')
        os.makedirs(pasta_barcodes, exist_ok=True)

        #gera o código de barra
        ean = barcode.get_barcode_class('ean13')
        ean_code = ean(str(self.codigo_ingresso.int)[:12], writer=ImageWriter())

        #caminho para salva o arquivo gerado
        file_path = os.path.join(pasta_barcodes, f"{self.codigo_ingresso}.png")
        ean_code.save(file_path)

        #salvar caminho no ImageField
        self.codigo_barras = f"barcodes/{self.codigo_ingresso}.png"

        super().save(*args, **kwargs)

