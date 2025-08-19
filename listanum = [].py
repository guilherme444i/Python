listanum = []
maior = 0
menor = 0

for i in range(0, 5):
    listanum.append(int(input(f'Digite um valor para a posição {i}: ')))
    if i == 0:
        maior = menor = listanum[i]
    else:
        if listanum[i] > maior:
            maior = listanum[i]
        if listanum[i] < menor:
            menor = listanum[i]

print('-=' * 30)
print(f'Os valores digitados foram: {listanum}')
print(f'O maior valor digitado foi: {maior} na posição ', end='')
for ind, num in enumerate(listanum):
    if num == maior:
        print(f'{ind}...', end='')
print()
print(f'O menor valor digitado foi: {menor} na posição ', end='')
for ind, num in enumerate(listanum):
    if num == menor:
        print(f'{ind}...', end='')
print()
print('-=' * 30)