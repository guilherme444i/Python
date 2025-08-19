num = []
pares = []
impares = []
while True:
    num.append(int(input('Digite um valor:')))
    resp= input('Quer continuar? [S/N]')
    if resp in 'Nn':
        break
for i, v in enumerate(num):
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
print('-='*30)
print(f'A lista completa é: {num}')
print(f'A lista de Pares é: {pares}')
print(f'A lista de Impares é: {Impares}')