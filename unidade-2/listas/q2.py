notas = []
soma = 0

for i in range(10):
    nota = int(input('Insira a nota do aluno {}: '.format(i)))

    soma += nota

    notas.append(nota)

media = soma / 10

print('A média da turma é: {:.2f}'.format(media))
print('Notas acima da média:')

for nota in notas:
    if nota > media:
        print('{:.1f}'.format(nota))