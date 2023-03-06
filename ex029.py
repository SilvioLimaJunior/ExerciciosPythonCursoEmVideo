from time import sleep
velo = float(input('Qual a velocidade do carro? '))
if velo > 80:
    multa = (velo - 80) * 7
    print('Você excedeu o limite de velocidade de 80km/h,\nE terá que pagar uma multa de R${:.2f}! '.format(multa))
    sleep(0.5)
    print('='* 60)
    sleep(0.5)
print('Faça uma boa viagem, dirija com segurança! ')

##1 Para fazer o radar eletrônico, criei uma variável recebendo input do usuário digitando a velocidade do veículo.
##2 Após isso, criei uma condição IF, se a a velocidade digitada for maior que 80 ele retorna a mensagem com a multa.
##3 Pra calcular a multa, peguei o valor digitado pelo usuário diminui 80 ( velocidade permitida ) e multipliquei pelo valor
#da multa por Km.

#O uso do sleep, foi mais estético para dar a sensação de interatividade! ( Aprendendo usar )