nome = str(input('Digite uma frase: ')).strip().upper()
print('A letra (A) apareceu {} vezes na sua frase.'.format(nome.count('A')))
print('A primeira letra (A) apareceu na posição {} '.format(nome.find('A') + 1))
print('A ultima letra (A) apareceu na posção {}'.format(nome.rfind('A')+ 1))


##1  criei uma variavel, tipo str, chamando input. Coloquei .strip para eliminar os espaços
#do começo e do fim digitado em vão, e upper para deixar tudo em maiúsculo;
##2 Para ver quantas vezes apareceu a letra "A" digitado pelo usuário, usei .count('A');
##3 Para ver em que posição a letra "A" apareceu primeiro, usei .find('A') + 1 - Afinal a contagem começa no 0;
##4 Para ver a posição em que a letra "A" apareceu por ultimo, utilizer rfind('A) + 1
# - ele verifica começando pela direita RIGHT e somei + 1 para adequar a posição correta.