# Notas do(a) estudante
notas = [6.0, 7.0, 9.0, 5.5, 8.0]
qualitativo = 0.5


# Não conseguimos aplicar o lambda em lista direto, é necessário utilizarmos junto a ela a função map
notas_atualizadas = map(lambda x: x + qualitativo, notas) # cria um tipo de dado chaado map, precisa usar list para converter
print(list(notas_atualizadas))