numero = int(input('Digite um número: '))

if numero < 0:
    print('O número deve ser maior que 0.')
else:
    fatorial = 1
    for i in range(numero, 0, -1):
        fatorial *= i
    
    print(fatorial)