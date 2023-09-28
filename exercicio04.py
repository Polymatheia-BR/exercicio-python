# Crie um algoritmo que receba 3 números e informe qual o maior entre eles.

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: "))
maior = num1

if maior < num2:
    maior = num2

if maior < num3:
    maior = num3

print(f'O maior número é {maior}')