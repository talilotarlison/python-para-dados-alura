# Exemplo básico
frutas = ['maçã', 'banana', 'uva']
indice = frutas.index('banana') # Retorna 1
print(indice)

# Usando enumerate para pegar índice e valor
for i, fruta in enumerate(frutas):
    print(f"Índice: {i}, Fruta: {fruta}")
