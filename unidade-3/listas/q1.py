valores = input().split(',')

temNumeroDistinto = False

if len(valores) < 2:
    print('Não é possível determinar o segundo maior valor com menos de dois elementos.')
else:
    maior = float(valores[0])

    for i in valores:
        valor = float(i)

        if valor != maior:
            temNumeroDistinto = True

        if valor > maior:
            maior = valor

    print(valor) if temNumeroDistinto else print('Não é possível determinar o segundo maior valor com menos de dois valores distintos.')