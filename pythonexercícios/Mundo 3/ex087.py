matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = coluna3 = maior = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'Digite um valor para [{linha}, {coluna}]: '))
        if matriz[linha][coluna] % 2 == 0:
            pares += matriz[linha][coluna]
        coluna3 += matriz[linha][2]
        if coluna == 0:
            maior = matriz[1][coluna]
        else:
            if matriz[1][coluna] > maior:
                maior = matriz[1][coluna]

print('-='*30)
for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}] ', end='')
    print()

print('-='*30)
print(f'A soma dos valores pares é {pares}.')
print(f'A soma dos valores da terceira coluna é {coluna3}.')
print(f'O maior valor da segunda linha é {maior}.')
print('-='*30)