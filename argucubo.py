class Cubo:
    def __init__(self, valor):
        self.x = valor
        print('Metodo executado')

    def calcularCubo(self):
        cubo = self.x * self.x * self.x
        return f'Cubo calculado: {cubo}'

cubo = Cubo(int(input('Digite um valor para saber o Cubo: ')))
calculo = cubo.calcularCubo()
print(calculo)