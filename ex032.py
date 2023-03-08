from datetime import date
ano = int(input("Digite qualquer ANO e descubra se ele é um ano BISSEXTO\nou digite 0 para o ano atual: "))
if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {}, é um ano BISSEXTO :D ".format(ano))
else:
    print("O ano {}, não é um ano bissexto :(".format(ano))

#1 Para saber se o ano digitado pelo usuário é BISSEXTO ultilizei as regras:
#2 if ano % 4 == 0 ( se o resto da divisão do ano por 4 for 0 )
#3 and ano % 100 != 0 (anos divisível por 100 NÃO são Bissextos) -> Aqui ele exlui todos os múltiplos de 100
#4 or ano % 400 == 0 (inclui os números que são divisíveis por 400. )
# |-> Aqui ele volta somente os múltiplos de 100 que são múltiplo de 400, tornando eles BISSEXTOS!


#Importei do módulo datetime a funçao date, pra acaso ser digitado 0, o ano receber o ano atual, date.today().year
