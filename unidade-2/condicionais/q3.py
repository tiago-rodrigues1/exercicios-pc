salario = float(input('Qual o valor do seu salário?'))
finaciamento = float(input('Qual o valor do financiamento?'))

pode_financiar = finaciamento <= (salario * 5)

print("Financiamento Concedido!") if pode_financiar else print("Financiamento Negado!")
print("Obrigado por nos consultar")