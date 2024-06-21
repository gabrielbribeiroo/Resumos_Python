def lin():
    print('-'*23)
# Programa principal
lin()
print('   CURSO EM VÍDEO   ')
lin()
print('   APRENDA PYTHON   ')
lin()
print('   GUSTAVO GUANABARA ')
lin()


def titulo(txt):
    print('-'*23)
    print(txt)
    print('-'*23)
titulo('   CURSO EM VÍDEO   ')
titulo('   PYTHON É MUITO BOM!   ')
titulo('   OI!  ')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma A + B = {s}')
# Programa principal
soma(4, 5)
soma(8, 9)
soma(2 ,1)
soma(4,1)
soma(b=4, a=5)
soma(7, 2)


def contador(* num):
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números.')
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM!')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)


def somavalores(* valor):
    s = 0
    for num in valor:
        s += num
    print(f'Somando os valores {valor} temos {s}')
somavalores(5, 2)
somavalores(2, 9, 4)