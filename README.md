# Projeto Ticketeria

## Descrição
Criamos uma API em Django REST Framework para gerenciar a compra e validação de ingressos para eventos. 
A API permite que usuários comprem ingressos informando CPF e ID do evento, e gera automaticamente um código de 
barras e um UUID único para cada ingresso.

## Funcionalidade
Clientes (Cliente)
 - Cadastro de clientes com nome, CPF, e-mail e telefone.
 - CPF é único para garantir que cada cliente seja identificado corretamente.

Eventos (Evento)
 - Cadastro de eventos com nome, data e local.
 - Ingressos (Ingresso)
 - Compra de ingressos informando CPF e ID do evento.
 - O sistema vincula o ingresso ao cliente correspondente.
 - Geração automática de UUID para cada ingresso.
 - Criação e armazenamento de código de barras para cada ingresso.

Ingressos (Ingresso)
 - Compra de ingressos informando CPF e ID do evento.
 - O sistema vincula o ingresso ao cliente correspondente.
 - Geração automática de UUID para cada ingresso.
 - Criação e armazenamento de código de barras para cada ingresso.


