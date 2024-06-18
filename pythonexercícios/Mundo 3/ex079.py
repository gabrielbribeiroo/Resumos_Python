num = []

while True:
    n = int(input('Digite um valor: '))

    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    if resp in 'N':
        break

print('-='*30)
print(f'Você digitou os valores {sorted(num)}')