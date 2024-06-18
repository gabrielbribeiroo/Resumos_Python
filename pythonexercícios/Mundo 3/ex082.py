num = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break
pares.sort()
impares.sort()
print('-='*30)
print(f'A lista completa é {num}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')