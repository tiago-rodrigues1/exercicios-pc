s = int(input())
t = int(input())
f = int(input())

def get_horario(partida, duracao, fuso):
    chegada = abs(partida + duracao + fuso)

    if chegada >= 24:
        chegada -= 24

    print('Hora de saída:', partida)
    print('Hora de chegada:', chegada)

get_horario(s, t, f)