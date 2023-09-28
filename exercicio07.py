# Faça um código que receba o valor da base e da altura de um triângulo e calcule sua área.
# Usando a fórmula A = (base x Altura) / 2

altura = float(input("Digite a altura: "))
while altura == 0:
    altura = float(input("Digite um valor diferente de 0 para a altura: "))

base = float(input("Digite a base: "))
while base == 0:
    base = float(input("Digite um valor diferente de 0 para a altura: "))

area = (base * altura) / 2
print(f'A área do triangulo é {area}')