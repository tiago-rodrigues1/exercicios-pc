n = int(input())

def get_level(velocidade: int):
    if velocidade < 10:
        return 1
    elif velocidade < 20:
        return 2
    else:
        return 3

maior = 0

for i in range(n):
    velocidade = int(input())

    level = get_level(velocidade)

    if level > maior:
        maior = level


print('Level', maior)