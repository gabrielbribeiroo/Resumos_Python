# if carro.esquerda():
    # bloco 1

# elif carro.direita():
    # bloco 2

# elif carro.ré():
    # bloco 3

# else:
    # bloco 4

# Condição aninhada
nome = str(input('Qual é o sue nome? '))
if nome == 'Gabriel':
    print('Que nome bonito! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil. ')
elif nome in 'Ana Claúdia Jéssica Juliana Luiza':
    print('Belo nome feminino. ')
else:
    print('Seu nome é bem normal. ')
print('Tenha um bom dia, {}! '.format(nome))
