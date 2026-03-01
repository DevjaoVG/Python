"""
Desmonstração de tratamento de exceções em Python com try, except, else e finally.
"""

# Exemplo de tratamento de exceções
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero
except ValueError:
    print("Erro: valor inválido.")
else:
    print(f"Resultado da divisão: {resultado}")
finally:
    print("Execução concluída.")