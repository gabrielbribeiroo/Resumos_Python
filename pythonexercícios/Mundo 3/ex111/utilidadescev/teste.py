import moeda

p = float(input('Digite o preço: R$'))
r = str(input('Deseja aumentar ou diminuir por uma taxa [S/N]? ')).upper().strip()[0]
i = 0
if r == 'S':
    t = str(input('Aumentar ou Diminuir [A/D]? ')).upper().strip()[0]
    if t == 'A':
        i = float(input('Qual a taxa de aumento? '))
    elif t == 'D':
        i = float(input('Qual a taxa de redução? '))
    else:
        print('ERRO! Tente novamente.')
    moeda.resumo(p, i, t, True)
else:
    moeda.resumo(p, i, '', True)
print(f'{"<<< FIM DO PROGRAMA >>>".center(30)}')