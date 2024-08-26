coordenadas_retangulo = input().split(" ")
coordenadas_ponto = input().split(" ")

x_top = float(coordenadas_retangulo[0])
y_top = float(coordenadas_retangulo[1])
x_bottom = float(coordenadas_retangulo[2])
y_bottom = float(coordenadas_retangulo[3])

x_ponto = float(coordenadas_ponto[0])
y_ponto = float(coordenadas_ponto[1])

if y_ponto > y_bottom or y_ponto < y_top or x_ponto < x_top or x_ponto > x_bottom:  
    print('Fora!')
else:   
    print('Dentro!')
