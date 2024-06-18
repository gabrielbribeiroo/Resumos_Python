ficha = list()

while True:
    nome = str(input('Nome: ')).capitalize()
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()
    if resp == 'N':
        break
    
print('-='*30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*25)
for indice, aluno in enumerate(ficha):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>7.1f}')
while True:
    print('-'*25)
    opcao = int(input('Mostrar notas de qual aluno? [999 PARA PARAR] '))
    if opcao == 999:
        print('FINALIZANDO...')
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} são {ficha[opcao][1]}')
print('<<< VOLTE SEMPRE >>>')