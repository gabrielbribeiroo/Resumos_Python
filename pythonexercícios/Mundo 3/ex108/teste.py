import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')

r = str(input('Deseja aumentar ou diminuir por uma taxa [S/N]? ')).upper().strip()[0]
if r == 'S':
    t = str(input('Aumentar ou Diminuir [A/D]? ')).upper().strip()[0]
    if t == 'A':
        i = float(input('Qual a taxa de aumento? '))
        print(f'Aumentando {i}% de {moeda.moeda(p)}, teremos {moeda.moeda(moeda.aumentar(p, i))}.')
    elif t == 'D':
        i = float(input('Qual a taxa de redução? '))
        print(f'Diminuindo {i}% de {moeda.moeda(p)}, teremos {moeda.moeda(moeda.diminuir(p, i))}.')
    else:
        print('ERRO! Tente novamente.')
print('<<< FIM DO PROGRAMA >>>')