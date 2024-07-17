distancia = int(input('Qual é a distância da viagem de ida e volta em quilômetros?'))
km_por_litro = float(input('Quantos quilômetros o carro percorre com cada litro de combustível?'))
preco_gasolina = float(input('Qual é o preço em reais por litro de combustível?'))

gasolina_usada = distancia / km_por_litro
valor_viagem = gasolina_usada * preco_gasolina

print('O valor em reais para realizar a viagem pretendida é ' + str(valor_viagem))
