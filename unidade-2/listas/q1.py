confirmados = ['Daniel', 'Aluizio', 'Isabel', 'Teles', 'Eduardo']

print('Lista de convidados confirmados:')

for i in confirmados:
    print(i)

nome = input('\nDigite o nome do convidado: ')

pode_entrar = 0

for confirmado in confirmados:
    if nome == confirmado:
        pode_entrar = 1
        break

if pode_entrar:
    print(nome, 'está na lista, acesso permitido!')
else:
    print(nome, 'não está na lista, acesso negado!')