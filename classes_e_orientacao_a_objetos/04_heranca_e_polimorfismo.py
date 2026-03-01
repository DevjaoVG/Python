"""
Demonstra de Herança e Polimorfismo em Python, utilizando classes base e subclasses.
"""

# Classe base
class Animal:
    def __init__(self, nome):
        self.nome = nome

    def falar(self):
        return "O animal faz um som."

# Subclasse Cachorro que herda da classe Animal
class Cachorro(Animal):
    def falar(self):
        return "O cachorro late."

# Subclasse Gato que herda da classe Animal
class Gato(Animal):
    def falar(self):
        return "O gato mia."


# Criando instâncias das subclasses
cachorro = Cachorro("Rex")
gato = Gato("Mia")

# Demonstrando o polimorfismo
animais = [cachorro, gato]
for animal in animais:
    print(f"{animal.nome} diz: {animal.falar()}")