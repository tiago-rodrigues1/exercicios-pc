quantidade = int(input('Digite a quantidade de itens recicláveis entregues: '))

pontuacao = quantidade
lista = []
bonus = 0

for i in range(quantidade + 1):
    if i % 2 != 0 and i % 3 == 0:
        lista.append(i)

lista.sort()

tamanho = len(lista)

if tamanho == 0:
    bonus = 0
elif tamanho % 2 == 0:
    index1 = (tamanho // 2) - 1
    index2 = index1 + 1
    
    bonus = (lista[index1] + lista[index2]) // 2
else:
    index = ((tamanho + 1) // 2) - 1

    bonus = lista[index]

pontuacao += bonus

print('\nLista:')
print(lista)
print('Bônus: {:.0f}'.format(bonus))
print('Pontuação final: {:.0f}'.format(pontuacao))
