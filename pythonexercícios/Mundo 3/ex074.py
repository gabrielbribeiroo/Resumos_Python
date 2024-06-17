# Números sorteados
from random import randint
número = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))  # tupla formada por 5 números sorteados entre 1 e 10
print(f'Eu sorteei os valores: {número}')
print(f'O maior valor sorteado foi {max(número)}')  # função max encontra o máximo valor
print(f'O menor valor sorteado foi {min(número)}')  # função min encontra o mínimo valor
