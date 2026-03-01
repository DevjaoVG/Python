"""
Desmonstração de classe e sua sintaxe básica em Python.
"""

# Definição de uma classe
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo de instância
        self.idade = idade

    def apresentar(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."


# Criando uma instância da classe Pessoa
pessoa1 = Pessoa("Alice", 30)
print(pessoa1.apresentar())