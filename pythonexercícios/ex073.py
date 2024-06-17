# Times de Futebol
times = ('Palmeiras', 'Internacional', 'Fluminense', 'Corinthians', 'Flamengo',
         'Athletico PR', 'Atlético MG', 'Fortaleza', 'São Paulo', 'América MG',
         'Botafogo', 'Santos', 'Goiás', 'Bragantino', 'Coritiba',
         'Cuiabá', 'Ceará', 'Atlético GO', 'Avaí', 'Juventude')  # tabela do brasileirão 2022
print('-=' * 15)
print(f'Lista de times do Brasileirão: {times}')
print('-=' * 15)
print(f'Os 5 primeiros colocados foram {times[0:5]}')  # mostra os times da posição 0 até a 4 (os 5 primeiros)
print('-=' * 15)
print(f'Os 4 últimos colocados e rebaixados foram {times[-4:]}')  # mostra os times da posição -4 até o final
print('-=' * 15)
print(f'Times em ordem alfabética: {sorted(times)}')  # mostra os times em uma tupla ordenada
print('-=' * 15)
print(f'O Santos está na {times.index("Santos")+1}ª posição')  # procura a posição do Santos e acrescenta 1
