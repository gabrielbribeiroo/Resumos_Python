print('= ' * 30)
print('{:^30} '.format('BANCO CEV '))
print('= ' * 30)
valor = int(input('Qual valor você quer sacar?  R$'))
total = valor
céd = 50
totalcéd = 0
while True:
    if total >= céd:
        total -= céd
        totalcéd += 1
    else:
        print(f'Total de {totalcéd} cédulas de R${céd} ')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totalcéd = 0
        if total == 0:
            break
print('= ' * 30)
print('Volte sempre ao BANCO CEV! Tenha um bom dia! ')
