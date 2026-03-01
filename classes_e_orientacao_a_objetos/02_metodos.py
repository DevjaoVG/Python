"""
Demonstração de métodos em Python.  
"""

# Classe carro
class Carro:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def exibir_informacoes(self):
        return f"Carro: {self.marca} {self.modelo}"

    def acelerar(self):
        return f"O {self.marca} {self.modelo} está acelerando!"


# Criando uma instância da classe Carro
carro1 = Carro("Toyota", "Corolla") 
print(carro1.exibir_informacoes())  # Chama o método para exibir informações do carro
print(carro1.acelerar())  # Chama o método para acelerar o carro