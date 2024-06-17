# Lista de Preços
print("-"*40)
print("          LISTAGEM DE PREÇOS           ")
print("-"*40)
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 4.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
for posicao in range(0, len(listagem)):
    if posicao % 2 == 0:
        print(f'{listagem[posicao]:.<30}', end="")
    else:
        print(f'R${listagem[posicao]:>7.2f}')
print("-"*40)


