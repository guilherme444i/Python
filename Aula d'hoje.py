nome = input("Diga seu nome: ")
turma = input("Diga a sua turma: ")
media = float(input("De 0 a 10, diga a nota do aluno: "))

if media < 5:
    print("Reprovado")
else:
    print("Aprovado")

if media < 6.0:
    conceito = 'F'
elif media < 7.0:
    conceito = 'D'
elif media < 8.0:
    conceito = 'C'
elif media < 9.0:
    conceito = 'B'
else:
    conceito = 'A'

print(f"Aluno: {nome} | Turma: {turma} | Nota: {media} | Conceito: {conceito}")