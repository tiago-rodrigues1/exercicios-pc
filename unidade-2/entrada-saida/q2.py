quantidade_multas = 2

multa = float(input('Qual é o valor original cobrado por cada multa?'))
juros = float(input('Qual é a porcentagem de juros cobrada pelo Detran?')) / 100
contribuintes = int(input('Quantos amigos irão contribuir com as despesas?'))

multa_com_juros = (multa * quantidade_multas) * (1 + juros)
valor_por_contribuinte = multa_com_juros / contribuintes

print('O valor em reais que cada amigo deverá pagar ao Detran é ' + str(round(valor_por_contribuinte, 5)))