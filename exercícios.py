class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_nome(self):
        print(f'O nome da pessoa é {self.nome}')

    def mostrar_idade(self):
        print(f'A idade da pessoa é {self.idade} anos')

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

pessoa1 = Pessoa(nome, idade)

pessoa1.mostrar_nome()
pessoa1.mostrar_idade()    