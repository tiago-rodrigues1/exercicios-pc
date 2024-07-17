numero = int(input('Qual é o número inteiro que deve ser utilizado para gerar a sequência?'))

anterior1 = numero - 1
anterior2 = anterior1 - 1

sucessor1 = numero + 1
sucessor2 = sucessor1 + 1

soma = anterior1 + anterior2 + numero + sucessor1 + sucessor2

print(anterior2, anterior1, numero, sucessor1, sucessor2, soma)