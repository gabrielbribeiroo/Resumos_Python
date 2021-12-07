from datetime import date
atual = date.today().year
nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento
print('Quem nasceu em {} tem {} anos em {} '.format(nascimento, idade, atual))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE! ')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento. '.format(saldo))
elif idade > 18:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos '.format(saldo))
    print('O seu alistamento foi em {}. '.format(ano))
