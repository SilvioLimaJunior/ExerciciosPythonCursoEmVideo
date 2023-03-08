#Preço da viagem
km = int(input('Qual a distância da sua viagem em Km ?'))

#if km <= 200:
#    pr = km * 0.50
#    print("O preço da sua viagem de {}km é de: R${:.2f}".format(km, pr))
#else:
#    pr = km * 0.45
#    print("O preço da sua viagem de {}Km é de: R${:.2f}".format(km, pr))

pr = km * 0.50 if km <= 200 else km * 0.45
print("O preço da sua viagem é R${:.2f}".format(pr))

#1 Para definir se o preço seria 0.50 ou 0.45 por Km fiz a condição do Km ser <= à 200
#2Fiz de dois modos, if else normal e de modo simplificado em uma linha (inline) que embora seja mais rápido,
#procuro optar pelo método tradicional, por questão estética visual. 