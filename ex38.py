# Recebemos duas demandas a respeito desse projeto com as notas dos estudantes:

# Criar uma lista da situação dos estudantes em que caso sua média seja maior ou igual a 6 receberá o valor "Aprovado" e caso contrário receberá o valor "Reprovado".

# Gerar uma lista de listas com:

# Lista de tuplas com o nome dos estudantes e seus códigos.

# Lista de listas com as notas de cada estudante.

# Lista com as médias de cada estudante.

# Lista da situação dos estudantes de acordo com as médias.

# Os dados que utilizaremos são os mesmos que geramos nas situações anteriores (nomes, notas, medias).

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

situacao = ["Aprovado" if media >= 6 else "Reprovado" for media in medias]
print(situacao)

cadastro = [x for x in [nomes, notas, medias]]
print(cadastro)