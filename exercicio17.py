macas_compradas = int(input('Digite quantas maçãs vão ser compradas: '))
preco = 1.30

if macas_compradas >= 12:
    preco = 1

total = macas_compradas * preco

print(f'O valor total da compra é de {total}')