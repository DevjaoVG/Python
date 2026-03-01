"""
Demosntração de funções.
"""

# Saudação
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo(a) ao curso de Python.")

saudacao("João")

# Soma
def soma(a, b):
    return a + b

resultado_soma = soma(5, 3)
print(f"A soma de 5 e 3 é: {resultado_soma}")

# funções lampda
multiplicacao = lambda x, y: x * y
resultado_multiplicacao = multiplicacao(4, 6)
print(f"A multiplicação de 4 e 6 é: {resultado_multiplicacao}")