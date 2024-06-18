num = []
while True:
    num.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break
print('-='*30)
print(f'Você digitou {len(num)} elementos.')
num.sort(reverse=True)
print(f'Os valores em ordem decrescente são {num}')
if 5 in num:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')