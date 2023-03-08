s1 = int(input('Digite o primeiro seguimento: '))
s2 = int(input('Digite o segundo seguimento: '))
s3 = int(input('Digite o terceiro seguimento: '))
if s1 < s2 + s3 and s2 < s3 + s1 and s3 < s2+ s1:
    print('Os seguimentos digitados PODEM formar um triângulo!')
else:
    print('Os seguimentos digitados NÃO formam triângulo.')

#1 Para definir se os três valores digitados pelo usuário pode formar um triângulo, fiz a condição que um valor tem que ser
#menor do que a soma dos outros dois valores. ( para todos digitados ) se não for então não pode formar triângulo.