num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#No codigo acima, variavél "u", ele vai pegar o número que o usuário digitar e fazer a divisão ineira por 1
#Após fazer a divisão inteira por um, ele irá dividir por 10 e o resto da divisão irá pra dentro da váriavél.
#E o mesmo acontece com a dezena, centena, milhar com valores ajustados conforme o codigo acima.

print('Unidade {}'.format(u))
print('Dezena {}'.format(d))
print('Centena {}'.format(c))
print('Milhar {}'.format(m))

#--------------------------------------------------------
#num = input('Digite um número: ')
#n = str(num)
#print('Ok, vamos analizar o número {}'.format(n))
#print('...')
#print('Unidades: {}'.format(n[3]))
#print('Dezenas: {}'.format(n[2]))
#print('Centena: {}'.format(n[1]))
#print('Milhar: {}'.format(n[0]))
## O código acima gera um erro quando não digitado os 4 números.
