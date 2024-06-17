# Análise de Dados
número = (int(input('Digite um número: ')),
          int(input('Digite outro número: ')),
          int(input('Digite mais um número: ')),
          int(input('Digite o último número: ')))  # tupla que vai guardar 4 valores digitados
print(f'Você digitou os valores ({número})')  # mostra todos os valores da tupla
print(f'O valor 9 apareceu {número.count(9)} vezes')  # mostra a quantidade de vezes que o número 9 apareceu na tupla
if 3 in número:  # se o número 3 está na tupla número
    print(f'O valor 3 apareceu na {número.index(3) + 1}ª posição')  # escreva a posição do valor 3 acrescentada de 1
else:  # senão
    print('O valor 3 não foi digitado em nenhuma posição')
print(f'Os valores pares digitados foram ', end='')
for num in número:  # para num na tupla número
    if num % 2 == 0:  # se o resto da divisão de num por 2 for 0 (se num par)
        print(num, end=' ')  # mostra os números pares
