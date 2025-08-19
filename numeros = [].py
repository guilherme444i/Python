numeros = []
while True:
    n = int(input('Digite um valor: '))
    if n not in numeros:
        numeros.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print(f'Valor digitado {n}, já existe na lista.')

    r = str(input('Quer continuar? S/N '))
    if r in 'Nn':
        break

print('-=' * 30)
print(f'Você digitou: {numeros}')
numeros.sort()
print(f'Os valores em ordem crescente: {numeros}')
numeros.sort(reverse=True)
print(f'Os valores em ordem decrescente: {numeros}')