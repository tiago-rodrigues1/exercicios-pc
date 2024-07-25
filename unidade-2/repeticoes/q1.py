import math

print('Insira a taxa do exame para 10 pacientes:')

soma = 0
produto = 1
soma_inversos = 0

for i in range(10):
    taxa = float(input())

    soma += taxa
    produto *= taxa
    soma_inversos += 1/taxa

media_aritmetica = soma / 10
media_geometrica = math.pow(produto, 0.1)
media_harmonica = 10 / soma_inversos

erro_harmonica = (media_harmonica - media_aritmetica) / media_aritmetica
erro_geometrica = (media_geometrica - media_aritmetica) / media_aritmetica
erro_medio = (erro_harmonica + erro_geometrica) / 2


print('Média aritmética: {:.2f}%'.format(media_aritmetica))
print('Média harmônica: {:.2f}%'.format(media_harmonica))
print('Média geométrica: {:.2f}%'.format(media_geometrica))
print('Erro médio:{:.2f}%'.format(erro_medio * 100))
