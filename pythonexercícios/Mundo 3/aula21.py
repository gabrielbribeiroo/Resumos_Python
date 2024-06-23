help(print)
print(input.__doc__)
help(input)

from time import sleep
def contador(i, f, p):
    """
        -> Faz uma contagem e mostra na tela
        :param i: início da contagem
        :param f: fim da contagem
        :param p: passo da contagem
        :return: sem retorno
        Função criada por Gabriel Ribeiro
    """
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')
contador(2, 10, 2)
contador(0, 100, 10)
help(contador)

def somar(a=0, b=0, c=0):
    """
        -> Faz a soma de três valores e mostra o resultado na tela.
        :param a: o primeiro valor
        :param b: o segundo valor
        :param c: o terceiro valor
        Função criada por Gabriel Ribeiro
    """
    s = a + b + c
    print(f'A soma vale {s}')
somar(3, 2, 5)
somar(8, 4)
somar()
somar(3, 3, 5)
somar(b=4, c=2)
somar(c=3, a=2)

def teste():
    print(f'Na função teste, n vale {n}')
n = 2
print(f'No programa principal, n vale {n}')
teste()

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}')
n1 = 2
funcao()
print(f'N1 fora vale {n1}')

def soma(a=0, b=0, c=0):
    s = a + b + c
    return s
r1 = soma(3, 2, 5)
r2 = soma(2, 2)
r3 = soma(6)
print(f'Os resultados foram {r1}, {r2}, {r3}')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é igual a {fatorial(n)}')
f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('É ímpar!')