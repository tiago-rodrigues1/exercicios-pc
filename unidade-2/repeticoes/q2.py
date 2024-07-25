print('Insira a quantidade de itens e o valor unitário. Cada item deve estar em uma linha separada. Para encerrar, digite o valor -1.')

valor_total = 0
quantidade_total = 0

while True:
    entrada = input()
    
    if entrada == "-1": break

    [quantidade, valor] = entrada.split(' ')

    quantidade_num = int(quantidade)
    valor_num = float(valor)

    valor_total += quantidade_num * valor_num
    quantidade_total += quantidade_num

print(quantidade_total, 'itens precisam ser comprados e o total é R$ {:.2f}'.format(valor_total))