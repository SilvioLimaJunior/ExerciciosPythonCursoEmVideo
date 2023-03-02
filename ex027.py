n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('É um prazer te conhecer! ')
print('Seu primeiro nome é {} '.format(nome[0]))
print('Seu último nome é: {} '.format(nome[len(nome)-1]))

# 1 - Para conseguir identificar partes do nome, criei uma variavel com o nome digitado.split
# 2 - Para identificar o primeiro nome, utilizei nome[0], ou seja vai me entregar o elemento da variavel que criei para repartir
# o nome na posição 0.
# 3 - Para identificar o último nome, utilizei nome na posição [len(nome)-1], ou seja, vai pegar o número de partes que o nome
# tem e subtrair 1 me entregando a ultima posição afinal o elemento começa no 0.