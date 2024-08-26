medidas = input().split(" ")

a = float(medidas[0])
b = float(medidas[1])
c = float(medidas[2])

mensagem = ''

if a >= (b + c):
    print('NAO FORMA TRIANGULO')
else:
    if (a**2) == ((b**2) + (c**2)):
        print('TRIANGULO RETANGULO')

    if (a**2) > ((b**2) + (c**2)):
        print('TRIANGULO OBTUSANGULO')

    if (a**2) < ((b**2) + (c**2)):
        print('TRIANGULO ACUTANGULO')

    if a == b and b == c:
        print('TRIANGULO EQUILATERO')
    elif a == b or b == c or a == c:
        print('TRIANGULO ISOCELES')