quantidade_pessoas = int(input('Qual o número de pessoas?'))

soma = 0

for i in range(quantidade_pessoas):
    idade = int(input('Digite a idade da pessoa {}: '.format(i + 1)))

    soma += idade

media = soma / quantidade_pessoas

print('A média de idade das pessoas é {} anos'.format(round(media)))