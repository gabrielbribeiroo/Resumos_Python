# lanche = 'Hambúrguer'
# print(lanche) --> mostra hambúrguer

lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')  # tupla (variável composta) lanche
print(lanche)  # mostra todos da variável lanche
print(lanche[1])  # tupla lanche na posição 1 (suco)
print(lanche[3])  # tupla lanche na posição 3 (pudim)
print(lanche[-2])  # tupla lanche na posição -2 (pizza)
print(lanche[1:3])  # tupla lanche no pedaço/fatiamento de 1 até 3, exluindo a posição 3 (suco, pizza)
print(lanche[2:])  # tupla lanche da posição até o final (pizza, pudim)
print(lanche[:2])  # tupla lanche do início até a posição 2, desconsiderando a última
print(lanche[-3:])  # tupla lanche da posição -3 até o final (suco, pizza, pudim)

# Tuplas são imutáveis
# lanche[1] = 'Refrigerante'
# print(lanche[1])

for comida in lanche:  # para cada comida em lanche....
    print(f'Eu vou comer {comida}')  # escreva eu vou comer tal coisa
print('Comi pra caramba!')

print(len(lanche))  # mostra o comprimento da tupla lanche

for contador in range(0, len(lanche)):  # para contador do intervalo de 0 até a quantidade de termos de lanche
    print(
        f'Eu vou comer {lanche[contador]} na posição {contador}')  # escreva eu vou comer o lanche na posição
    # contador na posição contador...
print('Comi pra caramba!')

for posição, comida in enumerate(lanche):  # mostra a comida e a posição enumeradas da tupla lanche
    print(f'Eu vou comer {comida} na posição {posição}')

print(sorted(lanche))  # mostre o lanche organizado/em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a  # tupla c que recebe a soma de b com a
print(a)  # mostra todos os elementos da tupla a
print(b)  # mostra todos os elementos da tupla b
print(c)  # junta as tuplas b e a
print(len(c))  # tamanho da tupla c
print(c.count(5))  # quantidade de vezes que aparece o número 5 na tupla c
print(c.count(9))  # quantidade de vezes que aparece o número 9 na tupla c
print(c.index(8))  # indica a primeira ocorrência da posição do 8
print(c.index(5, 1))  # indica a posição do 5 a partir da posição 1


pessoa = ('Gustavo', 39, 'M', 99.88)
del pessoa  # deleta da memória a tupla pessoa
# não se pode deletar um item específico da tupla, mas pode deletá-la por inteiro


