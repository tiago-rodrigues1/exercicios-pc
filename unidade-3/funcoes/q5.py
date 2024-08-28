[n, d, u] = input().split(' ')

celulas = []

for i in range(int(n)):
    indice = int(input())
    celulas.append(indice)

def get_range(n, cells, distance, user):
    cell_from = user - distance
    cell_to = user + distance

    valid_indexes = []
    for i in range(n):
        if cells[i] >= cell_from and cells[i] <= cell_to:
            valid_indexes.append(cells[i])
    
    return valid_indexes

area = get_range(int(n), celulas, int(d), int(u))

print(str(area).strip('[]').replace(',', '')) if len(area) > 0 else print('USUARIO DESCONECTADO')