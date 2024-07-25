temperaturas = []

for i in range(1, 6, 1):
    entrada = int(input('Insira a temperatura do ponto {}: '.format(i)))

    temperaturas.append(entrada)

temperaturas.sort()

index_from = 0
index_to = 1

for i in range(4):
    intervalo = '[' + str(temperaturas[index_from]) + ', ' + str(temperaturas[index_to]) + '] = '

    for j in range(temperaturas[index_from], temperaturas[index_to] + 1):
        intervalo += str(j)

        if j != temperaturas[index_to]:
            intervalo += ','

    print(intervalo)

    index_from += 1
    index_to += 1
