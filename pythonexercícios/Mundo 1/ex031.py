distância = float(input('Qual é a distância da sua viagem: '))
print('Você está prestes a começar uma viagem de {}km. '.format(distância))
preço = distância * 0.5 if distância <= 200 else distância * 0.45
print('E o preço de sua passagem será de R${:.2f} '.format(preço))
