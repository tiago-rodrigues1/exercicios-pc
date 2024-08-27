n = int(input())

for i in range(n):
    quant_alunos = int(input())
    fila = input().split(" ")

    fila = list(map(int, fila))

    nao_troca = 0
    
    fila_nao_ordenada = fila.copy()
    fila.sort(reverse=True)

    for j in range(len(fila)):
        if fila[j] == fila_nao_ordenada[j]:
            nao_troca += 1

    print(nao_troca)

    