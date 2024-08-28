n = int(input())

valores = []
indices = []

total = 0

for i in range(n):
    [valor, indice] = input().split(" ")

    total += float(valor)

petisco = int(total * 0.1)
total -= petisco



ganhador = input()

