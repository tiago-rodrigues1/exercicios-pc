largura1 = float(input('Qual é a largura do lote 1?'))
comprimento1 = float(input('Qual é o comprimento do lote 1?'))

largura2 = float(input('Qual é a largura do lote 2?'))
comprimento2 = float(input('Qual é o comprimento do lote 2?'))

largura3 = float(input('Qual é a largura do lote 3?'))
comprimento3 = float(input('Qual é o comprimento do lote 3?'))

largura4 = float(input('Qual é a largura do lote 4?'))
comprimento4 = float(input('Qual é o comprimento do lote 4?'))

area1 = largura1 * comprimento1
area2 = largura2 * comprimento2
area3 = largura3 * comprimento3
area4 = largura4 * comprimento4

area_total = area1 + area2 + area3 + area4

print('A área total do terreno é {:.1f} m2'.format(area_total))