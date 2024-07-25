numero_texto = input()


is_par = int(numero_texto) % 2 == 0
is_palindromo = 1

inicio = 0
fim = len(numero_texto) - 1

for i in range(len(numero_texto) // 2):
    if (numero_texto[inicio] != numero_texto[fim]):
        is_palindromo = 0

    inicio += 1
    fim -= 1

msg = " é um palíndromo e é " if is_palindromo else " não é um palíndromo e é "
msg += "par." if is_par else "ímpar."

print('O número ' + numero_texto + msg)