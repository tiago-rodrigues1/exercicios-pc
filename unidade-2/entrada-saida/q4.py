import math

salario_inicial = float(input('Qual é o salário mensal inicial?'))

poncentagem_para_poupar = 0.5 

ano1 = salario_inicial * poncentagem_para_poupar * 12
novo_salario = salario_inicial * 1.05

ano2 = novo_salario * poncentagem_para_poupar * 12
novo_salario = novo_salario * 1.05

ano3 = novo_salario * poncentagem_para_poupar * 12

total = ano1 + ano2 + ano3

print('O valor acumulado em 3 anos é de {:.1f}'.format(total))