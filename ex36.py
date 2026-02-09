# A zip() é uma função embutida do Python que recebe um ou mais iteráveis (lista, string, dict, etc.) e retorna-os como um iterador de tuplas onde cada elemento dos iteráveis são pareados. Ela é útil para fazer iterações simultâneas em várias listas.

# A função zip() pode ser usada em conjunto com outras funções do Python, como map() e filter(), para criar soluções elegantes e concisas para certos problemas. Vamos fazer um simples teste para verificar esse comportamento:

id = [1, 2, 3, 4, 5]
regiao = ["Norte", "Nordeste", "Sudeste", "Centro-Oeste", "Sul"]

mapa = list(zip(id, regiao))
print(mapa)