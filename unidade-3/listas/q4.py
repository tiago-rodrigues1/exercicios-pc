lista = input().strip('[]').split(",")
item_remover = input()
item_substituir = input()

temNoInventario = False

for i in range(len(lista)):
    if lista[i].strip() == item_remover:
        lista[i] = item_substituir
        temNoInventario = True

print(lista) if temNoInventario else print('Item não presente no inventário.')