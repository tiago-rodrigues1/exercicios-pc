x = int(input())
z = int(input())

while z <= x:
    z = int(input())

quant = 0
soma = 0

while soma <= z:
    soma += x
    x += 1
    quant += 1
    

print(quant)