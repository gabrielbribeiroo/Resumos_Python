salário = float(input('Qual é o salário do seu funcionário? '))
aumento = salário * 1.10 if salário > 1250.00 else salário * 1.15
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora. '.format(salário, aumento))
