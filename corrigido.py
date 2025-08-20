aluno = {}
aluno['nome'] = input('Nome do aluno: ')
aluno['média'] = float(input(f'Média do {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif 4 <= aluno['média'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-='*30)

for k, v in aluno.items():
    print(f' -> {k} é igual a {v}')

print('-='*30)