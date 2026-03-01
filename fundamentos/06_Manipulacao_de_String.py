"""
Demonstração de manipulação de string
"""

# Indexação e fatiamento de strings
texto = "Olá, Mundo!"
print(texto[0])  # Imprime 'O'
print(texto[7:12])  # Imprime 'Mundo'

# Métodos (upper(), lower(), split() e replace.)
texto = "Olá, Mundo!"
print(texto.upper())  # Converte para maiúsculas
print(texto.lower())  # Converte para minúsculas
print(texto.split())  # Divide a string em uma lista de palavras
print(texto.replace("Mundo", "Python"))  # Substitui "Mundo" por "Python"

# F-strings
nome = "Alice"
idade = 30
print(f"Meu nome é {nome} e eu tenho {idade} anos.") # Usando f-string para formatar a string
