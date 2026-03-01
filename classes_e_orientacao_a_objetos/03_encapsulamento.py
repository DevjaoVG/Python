"""
Demonstração de Encapsulamento em Python, utilizando atributos privados e métodos de acesso.
"""

# classe conta bancaria
class ContaBancaria:
    def __init__(self, titular, saldo_inicial): 
        self.titular = titular  # Atributo público
        self.__saldo = saldo_inicial  # Atributo privado
    
    # Método público para consultar o saldo
    def consultar_saldo(self): 
        return f"Saldo atual: R${self.__saldo}"

    # Metodo privado para realizar um depósito
    def __depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
            return f"Depósito de R${valor} realizado com sucesso."
        else:
            return "Valor de depósito inválido."


conta = ContaBancaria("João", 1000)

# Tentando acessar o saldo diretamente (isso causará um erro)
# print(conta.__saldo)  # Isso causará um erro, pois __saldo é privado. Para alterar o saldo, devemos usar um método público ou privado da classe.

# Usando metodo privado para realizar um depósito (isso também causará um erro, pois __depositar é privado)
# print(conta.__depositar(500))

