class Carro:
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
    def exibir(self):
       print(f'{self.marca} : {self.modelo} : {self.ano}')

Carro1 = Carro ('Toyota', 'Corolla', 2020)
Carro1.exibir()
Carro2 = Carro('Ferrari', 'F40', 1987)
Carro2.exibir()