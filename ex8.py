# Recebendo as notas e calculando a média ponderável
N1 = float(input("Digite a 1ª nota do(a) estudante: "))
N2 = float(input("Digite a 2ª nota do(a) estudante: "))
N3 = float(input("Digite a 3ª nota do(a) estudante: "))

media_ponderavel = lambda x, y, z: (x * 3 + y * 2 + z * 5)/10
media_estudante = media_ponderavel(N1, N2, N3)
print(media_estudante)