# Crie um algoritmo que leia um número e diga se ele é par ou ímpar

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f'O número {num} é par')
else:
    print(f'O número {num} é impar')