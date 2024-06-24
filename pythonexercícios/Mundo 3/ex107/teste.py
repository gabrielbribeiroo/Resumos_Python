import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')

r = str(input('Deseja aumentar ou diminuir por uma taxa [S/N]? ')).upper().strip()[0]
if r == 'S':
    t = str(input('Aumentar ou Diminuir [A/D]? ')).upper().strip()[0]
    if t == 'A':
        i = float(input('Qual a taxa de aumento? '))
        print(f'Aumentando {i}% de R${p}, teremos {moeda.aumentar(p, i)}.')
    elif t == 'D':
        i = float(input('Qual a taxa de redução? '))
        print(f'Diminuindo {i}% de R${p}, teremos {moeda.diminuir(p, i)}.')
    else:
        print('ERRO! Tente novamente.')
print('<<< FIM DO PROGRAMA >>>')