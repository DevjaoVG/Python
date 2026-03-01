"""
Demonstração de coleções em Python, incluindo listas, tuplas, conjuntos e dicionários.
"""

# Listas
minha_lista = [1, 2, 3, 4, 5]
print("Lista:", minha_lista)

# Manipulação e metodos de listas
minha_lista.append(6)  # Adiciona um elemento ao final da lista
print("Lista após append:", minha_lista)
minha_lista.remove(3)  # Remove o elemento 3 da lista
print("Lista após remove:", minha_lista)    
minha_lista.sort()  # Ordena a lista
print("Lista ordenada:", minha_lista)

# Dicionários
meu_dicionario = {"nome": "Alice", "idade": 30, "cidade": "São Paulo"}
print("Dicionário:", meu_dicionario)

# Manipulação e metodos de dicionários
meu_dicionario["profissão"] = "Engenheira"  # Adiciona um novo par chave-valor
print("Dicionário após adição:", meu_dicionario)
print("Valores do dicionário:", meu_dicionario.values())  # Exibe os valores do dicionário
print("Chaves do dicionário:", meu_dicionario.keys())  # Exibe as chaves do dicionário

# Conjuntos
meu_conjunto = {1, 2, 3, 4, 5}
print("Conjunto:", meu_conjunto)

# Manipulação e metodos de conjuntos
meu_conjunto.add(6)  # Adiciona um elemento ao conjunto 
print("Conjunto após add:", meu_conjunto)
meu_conjunto.remove(2)  # Remove o elemento 2 do conjunto
print("Conjunto após remove:", meu_conjunto)