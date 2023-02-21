pr = float(input('Qual o preço atual do produto? R$'))
ddd = float(input('Qual o valor do desconto? % '))
desc = pr * ddd / 100
npr = pr - desc

print('O produto de R${:.2f} com {:.0f}% de desconto (ou seja R${:.2f} de desconto), \nsairá por: R${:.2f}'.format(pr, ddd, desc, npr))

