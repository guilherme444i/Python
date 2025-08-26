class Dinheiro:
    def __init__(self, valor_depositado):
        self.valor = valor_depositado
        self.saldo = valor_depositado
        print("Dinheiro depositado:", self.valor)

# Criando uma instância com valor depositado
valor_depositado = 200
deposito = Dinheiro(valor_depositado)