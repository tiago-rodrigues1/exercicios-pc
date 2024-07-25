numeros = []

while True:
    num = int(input())

    numeros.append(num)

    if num == 0:
        break


maior = numeros[0]

for i in numeros:
    if i > maior:
        maior = i

print('O recorde de pontos é', maior)
