n = 0
while n != 999:
    n = int(input('Digite um número: '))

n = cont = 0
while cont < 3:
    n = int(input('Digite um número: '))
    cont += 1

n = s = 0
while n != 999:
    n = int(input('Digite um número: '))
    s += n
s -= 999
print('A soma vale {} '.format(s))

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
# print('A soma vale {} '.format(s))
print(f'A soma vale {s} ')

nome = 'José'
idade = 33
salário = 987.35
print(f'O {nome} tem {idade} anos e ganha R${salário:.2f}. ') #PYTHON 3.6+
print('O {} tem {} anos. '.format(nome, idade)) #PYTHON 3
print('O %s tem %d anos. ' % (nome, idade)) #PYTHON 2
