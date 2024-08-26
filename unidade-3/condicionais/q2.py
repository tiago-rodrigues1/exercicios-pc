compra = float(input('Qual o valor da compra?'))
modo_pagamento = input('Como gostaria de pagar à vista(V) ou à prazo (P)?')

if modo_pagamento == "V":
    compra = compra * 0.95

    print('Valor à pagar {:.1f}'.format(compra))
elif modo_pagamento == "P":
    compra = compra * 1.08
    parcela_mensal = compra / 3

    print('Valor à pagar: {:.1f}'.format(compra))
    print('Parcela 1: {:.1f}'.format(parcela_mensal))
    print('Parcela 2: {:.1f}'.format(parcela_mensal))
    print('Parcela 3: {:.1f}'.format(parcela_mensal))