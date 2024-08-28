n = int(input())

valores = []
indices = []
montantes = []

total = 0

for i in range(n):
    [valor, indice] = input().split(" ")

    valores.append(float(valor))
    indices.append(indice)

    total += float(valor)

ganhador = input()

apostas_vencedoras = 0
for i in range(n):
    montantes.append(0)

    if indices[i] == ganhador:
        apostas_vencedoras += valores[i]




petisco = int(total * 0.1)
total -= petisco




