velocidade = int(input('Qual é a velocidade atual do carro?'))

if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 7

    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h!')
    print('Você deve pagar uma multa de R$ {:.1f}'.format(multa))
else:
    print('Tenha um bom dia! Dirija com segurança!')
