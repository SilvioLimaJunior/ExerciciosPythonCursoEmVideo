dias = int(input('Quantos dias alugados? '))
km = int(input('Quantos KM rodados? '))
vd = dias * 60
kmr = km * 0.15
total = vd + kmr
print('O total a pagar é: R${:.2f}'.format(total))
