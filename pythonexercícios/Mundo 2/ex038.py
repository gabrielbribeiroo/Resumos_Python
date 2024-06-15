n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
if n1 > n2:
    print('O PRIMEIRO valor é maior ')
elif n2 > n1:
    print('O SEGUNDO valor é maior ')
elif n1 == n2:
    print('Não existe valor maior, os dois são iguais ')
else:
    print('Opção inválida. Tente novamente. ')
