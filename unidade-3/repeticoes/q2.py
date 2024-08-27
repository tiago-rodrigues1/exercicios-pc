maior_gasto = 0

while True:
    gasto = float(input('Insira o valor gasto (ou 0 para terminar): '))

    if gasto == 0:
        break

    if gasto > maior_gasto:
        maior_gasto = gasto


print('O seu maior gasto hoje foi R$ {:.1f}'.format(maior_gasto)) if maior_gasto != 0 else print('Você não teve gastos hoje!')
