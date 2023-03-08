sal = float(input('Qual o salário do funcionário? '))
if sal > 1250:
    nsal = (sal * 0.1) + sal
    print('O salário que antes era R${:.2f} agora receberá um aumento de 10%, passando ser R${:.2f}.'.format(sal, nsal))
else:
    nsal = (sal * 0.15) + sal
    print('O salário que antes era R${:.2f} agora receberá um aumento de 15%, passando ser R${:.2f}.'.format(sal, nsal))

#1 Para encontrar a porcentagem que vou usar no aumento do salário, criei uma condição que se o salário for maior que 1250
#então ele passaria receber o salário + (sal * 0.1) 10%, se não seria salário + (sal +0.15) 15%.