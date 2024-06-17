maior = 0
menor = 0
for p in range(1, 6):
    p = float(input('Peso da {}ª pessoa '.format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if p > maior:
            maior = p
        if p < menor:
            menor = p
print('O maior peso lido foi de {}kg '.format(maior))
print('O menor peso lido foi de {}kg '.format(menor))
