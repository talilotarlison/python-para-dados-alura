# List Comprehension
# A List comprehension é uma forma simples e concisa de criar listas, sendo que essas listas seguirão alguns padrões, via condicionais, laços e outras expressões.

nomes = [('João', 'J720'), ('Maria', 'M205'), ('José', 'J371'), ('Cláudia', 'C546'), ('Ana', 'A347')]
medias = [9.0, 7.3, 5.8, 6.7, 8.5]

zip(nomes, medias)

estudantes = zip(nomes, medias)
print(estudantes)

estudantes = list(zip(nomes, medias))
print(estudantes)