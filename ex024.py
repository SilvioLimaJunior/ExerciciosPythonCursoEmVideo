#city = str(input('Qual a sua cidade? '))
#print('Santo' in city)

city = str(input('Qual a sua cidade? ')).strip()
print(city[:5].upper() == 'SANTO')

##1 Primeiro criei um input com tipo "str" pedindo ao usuario para digitar a cidade.
##2 Depois coloquei print para mostrar se a variável city [:5] (de 0 a 4 letra) se ele é igual a 'SANTO'
##.upper() faz com que de qualqer forma o usuário digite, esse comando vai jogar para maiúsculo
