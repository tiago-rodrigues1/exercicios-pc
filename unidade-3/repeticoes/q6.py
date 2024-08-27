t = int(input())

for i in range(t):
    dados = input().split()

    pa = int(dados[0])
    pb = int(dados[1])
    g1 = float(dados[2])
    g2 = float(dados[3])

    anos = 0

    while(pa <= pb):
        pa += int(pa * (g1 / 100))
        pb += int(pb * (g2 / 100))

        anos += 1

        if anos > 100:
            break
    
    print(anos, 'anos.') if anos <= 100 else print('Mais de 1 século.')
    