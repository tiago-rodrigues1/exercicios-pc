nota1 = float(input('Qual é a nota da primeira unidade?'))
nota2 = float(input('Qual é a nota da segunda unidade?'))
nota3 = float(input('Qual é a nota da terceira unidade?'))

media = ((nota1 * 2) + (nota2 * 3) + (nota3 * 4)) / 9
situacao = ""

if media >= 7:
    situacao = "aprovado"
elif media < 3:
    situacao = "reprovado"
else:
    situacao = "em prova final"

print(media)
print('Francisco está', situacao)
