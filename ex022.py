nome = str(input('Digite seu nome completo: ').strip())
print('Analizando o seu nome...')
print('O seu nome em letras maiúsculas é : {}'.format(nome.upper()))
print('O seu nome em letras minúsculas é: {}'.format(nome.lower()))
print('O total de letras do seu nome é: {} letras.'.format(len(nome) - nome.count(' ')))
# Abaixo primeira opção de descobrir o primeiro nome do usuário:
# print('O total de letras do seu primeiro nome tem: {} letras.'.format(nome.find(' ')))
# Abaixo a segunda opção de descobrir o primeiro nome do usuário:
separa = nome.split()
print('O seu nome tem {} letras.'.format(len(separa[0])))