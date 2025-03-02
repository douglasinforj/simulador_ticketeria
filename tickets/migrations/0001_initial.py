# Generated by Django 5.1.5 on 2025-02-04 23:58

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('cpf', models.CharField(max_length=14, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('telefone', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Evento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('data', models.DateTimeField()),
                ('local', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ingresso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ingresso', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('codigo_barras', models.ImageField(blank=True, null=True, upload_to='barcodes/')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.cliente')),
                ('evento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.evento')),
            ],
        ),
    ]
