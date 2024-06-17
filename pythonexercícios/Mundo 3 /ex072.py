# Número por Extenso
contador = ('zero', 'um', 'dois', 'três', 'quatro',
            'cinco', 'seis', 'sete', 'oito',
            'nove', 'dez', 'onze', 'doze',
            'treze', 'catorze', 'quinze', 'dezesseis',
            'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:   # enquanto for verdadeiro
    número = int(input('Digite um número na posição de 0 até 20: '))
    if 0 <= número <= 20:  # se o número digitado estiver entre 0 e 20
        break  # para
    print('Tente novamente. ', end='')  # não pula de linha depois do "tente novamente"
print(f'Você digitou o número {contador[número]}')  # mostra o número digitado por extenso, através da posição do número no contador
