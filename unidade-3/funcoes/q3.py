def is_primo(n: int):  
    if n % 2 == 0:
        return False

    qnt = 0
    for i in range(1, n + 1):
        qnt += n % i == 0

    return qnt == 2


n = int(input())

print('Número forma par de gêmeos') if is_primo(n) and is_primo(n + 2) else print('Número não forma par de gêmeos')