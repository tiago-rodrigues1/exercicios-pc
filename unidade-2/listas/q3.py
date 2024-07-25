meses = [
    'Janeiro',
    'Fevereiro',
    'Março',
    'Abril',
    'Maio',
    'Junho',
    'Julho',
    'Agosto',
    'Setembro',
    'Outubro',
    'Novembro',
    'Dezembro'
]

numero_mes = int(input('Digite um número entre 1 e 12 para selecionar um mês: '))

if numero_mes > 12 or numero_mes < 1:
    print('Erro: não existe mês de número {}. Por favor, digite um número entre 1 e 12.'.format(numero_mes))
else:
    print('O mês selecionado é: {}'.format(meses[numero_mes - 1]))