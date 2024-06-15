peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))
IMC = peso / (altura * altura)
print('O IMC dessa pessoa é de {:.1f} '.format(IMC))
if IMC < 18.5:
    print('Você está ABAIXO DO PESO normal ')
elif 25 > IMC > 18.5:
    print('PARABÉNS, você está na faixa de PESO NORMAL ')
elif 30 > IMC > 25:
    print('Você está em SOBREPESO ')
elif 40 > IMC > 30:
    print('Você está em OBESIDADE! ')
elif IMC > 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado! ')
