# Testando a mesma função para uma função lambda
nota = float(input("Digite a nota do(a) estudante: "))

qualitativo = lambda x: x + 0.5

print(qualitativo(nota))