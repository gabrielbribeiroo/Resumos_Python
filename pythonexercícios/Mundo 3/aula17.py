num = [2, 5, 9, 1]
num[2] = 3 # Listas são mutáveis
num.append(7) # Adiciona 7 ao final da lista num
num.sort() # Ordena os valores de forma crescente
num.sort(reverse=True) # Ordena os valores de forma decrescente
num.insert(2, 2) # Insere um elemento em determinada posição
num.remove(2) # Remove um elemento da lista (na primeira ocorrência)
if 5 in num:
    num.remove(5) # Remove o elemento apenas se estiver presente na lista
else:
    print('Não achei o número')
print(num) # Imprime a lista
print(f'Essa lista tem {len(num)} elementos.') # Imprime a quantidade de elementos da lista


valores = []
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c}, encontrei o valor {v}!')
print('Cheguei ao final da lista')


a = [2, 3, 4, 7]
b = a # Liga as duas listas
b = a[:] # Recebe todos os elementos da outra lista (apenas copia)
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')