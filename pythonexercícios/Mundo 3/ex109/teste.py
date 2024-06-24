import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')

r = str(input('Deseja aumentar ou diminuir por uma taxa [S/N]? ')).upper().strip()[0]
if r == 'S':
    t = str(input('Aumentar ou Diminuir [A/D]? ')).upper().strip()[0]
    if t == 'A':
        i = float(input('Qual a taxa de aumento? '))
        print(f'Aumentando {i}% de {moeda.moeda(p)}, teremos {moeda.aumentar(p, i, True)}.')
    elif t == 'D':
        i = float(input('Qual a taxa de redução? '))
        print(f'Diminuindo {i}% de {moeda.moeda(p)}, teremos {moeda.diminuir(p, i, True)}.')
    else:
        print('ERRO! Tente novamente.')
print('<<< FIM DO PROGRAMA >>>')