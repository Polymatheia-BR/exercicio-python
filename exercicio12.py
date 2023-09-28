# Escreva um algoritmo para ler o número total de eleitores de um município, o número de votos
# brancos, nulos e válidos. Calcular e escrever o percentual que cada um representa em relação
# ao total de eleitores.

eleitores = int(input("Digite o número total de eleitores: "))

votos_brancos = int(input("Digite a quantidade de votos brancos: "))
votos_nulos = int(input("Digite a quantidade de votos nulos: "))
votos_validos = int(input("Digite a quantidade de votos válidos: "))

percentual_brancos = (votos_brancos / eleitores) * 100
percentual_nulos = (votos_nulos / eleitores) * 100
percentual_validos = (votos_validos / eleitores) * 100

print(f'O percentual de votos brancos é {percentual_brancos}%')
print(f'O percentual de votos nulos é {percentual_nulos}%')
print(f'O percentual de votos válidos é {percentual_validos}%')