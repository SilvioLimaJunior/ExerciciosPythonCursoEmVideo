
from random import randint
pc = randint(0,5)
from time import sleep
print('=-=' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar....')
print('=-=' * 20)
n = int(input('Qual número pensei? '))
print('HUUUUM....')
sleep(1)
if n == pc:
    print('Parabéns, você acertou!!!')
else:
    print('ERROOOOOOOU!!! Eu pensei no número: {}'.format(pc))

##1 Para fazer o progrma "pensar" um número, ultilizei o método "randint" do módulo random, para a variavél pc receber
## um número aleatório gerado.

##2 Após isso criei uma condição pra caso o usuário digite o valor igual ao que foi "sorteado" pelo random, ele vença
##e se não ele perde.

##3 pra deixar justo, na linha em que se o usuário perder, coloquei um format mostrando o número "pensado" pelo computador.

