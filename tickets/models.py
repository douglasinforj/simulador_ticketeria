from django.db import models

import uuid
import barcode
from barcode.writer import ImageWriter


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
        #gera codigo de barra
        ean = barcode.get_barcode_class('ean13')
        ean_code = ean(str(self.codigo_ingresso.int)[:12], writer=ImageWriter())
        file_path = f"barcodes/{self.codigo_ingresso}.png"
        ean_code.save(file_path)
        self.codigo_barras = file_path

        super().save(*args, **kwargs)

