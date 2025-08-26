class Vendas:
    def __init__(self, nome):
        self.nome = nome
        self.vendas = 0

    def vendeu(self, vendas):
        self.vendas += vendas

    def bateu_meta(self, meta):
        if self.vendas >= meta:
            print(f'{self.nome} bateu a meta')
        else:
            print(f'{self.nome} não bateu a meta')

vendedor1 = Vendas('CJ da quebrada')
vendedor1.vendeu(600)
vendedor1.bateu_meta(500)

vendedor2 = Vendas ('Marcelo do tigrinho')
vendedor2.vendeu(1)
vendedor2.bateu_meta(2)