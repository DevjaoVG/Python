""""
Demonstra a sintaxe básica de Python, incluindo variáveis e tipos primitivos.
Autor: João
""""

# Tipos primitivos
idade = 25  # Tipo inteiro
altura = 1.75  # Tipo float
nome = "João"  # Tipo string    
is_estudante = True  # Tipo booleano

# Tipos Compostos
lista = [1, 2, 3, 4, 5]  # Tipo lista
tupla = (1, 2, 3)  # Tipo tupla
dicionario = {"nome": "João", "idade": 25}  #
iSet = {1, 2, 3}  # Tipo conjunto

# Imprimindo os valores e seus tipos
print(f"Idade: {idade}, Tipo: {type(idade)}")
print(f"Altura: {altura}, Tipo: {type(altura)}")
print(f"Nome: {nome}, Tipo: {type(nome)}")
print(f"É estudante? {is_estudante}, Tipo: {type(is_estudante)}")
print(f"Lista: {lista}, Tipo: {type(lista)}")
print(f"Tupla: {tupla}, Tipo: {type(tupla)}")
print(f"Dicionário: {dicionario}, Tipo: {type(dicionario)}")
print(f"Conjunto: {iSet}, Tipo: {type(iSet)}")