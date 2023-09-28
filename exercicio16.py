hora_inicio = int(input('Digite a hora de inicio da partida de xadrez: '))
hora_fim = int(input('Digite a hora do fim da partida de xadrez: '))

if hora_inicio > hora_fim:
    hora_inicio -= 24
    print(hora_fim - hora_inicio)
else:
    print(hora_fim - hora_inicio)