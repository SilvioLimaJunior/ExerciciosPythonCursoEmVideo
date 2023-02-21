from random import choice
n1 = str(input('Digite o primeiro nome: '))
n2 = str(input('Digite o segundo nome: '))
n3 = str(input('Digite o terceiro nome: '))
lista = [n1,n2,n3]
esc = choice(lista)
print('O escolhido foi: {} '.format(esc))


