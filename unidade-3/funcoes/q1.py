[n1, n2] = input().split(" ")

def get_soma_divisores (n):
    soma = 0

    for i in range(1, n):
        if n % i == 0:
            soma += i

    return soma

def is_amigos(a, b):
    soma_a = get_soma_divisores(a)
    soma_b = get_soma_divisores(b)

    return soma_a == b and soma_b == a

print('Sim') if is_amigos(int(n1), int(n2)) else print('Não')