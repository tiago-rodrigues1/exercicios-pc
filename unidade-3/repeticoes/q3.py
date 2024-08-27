n = int(input())

resultado =  []

for i in range(1,(n+1)):
    tmp = []
    count = i
    for j in range(n):
        tmp.append(abs(count))
        if(count == 1):
            count -= 3
        else:
            count -= 1
    resultado.append(tmp)

for i in range(n):
    tx = ''
    for j in range(n):
        tx += str(resultado[i][j]) + " "
    print(tx)
print("")