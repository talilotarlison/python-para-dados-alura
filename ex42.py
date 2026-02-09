# finally
# O try corresponde ao fluxo normal, except ao fluxo de exceção, e else para o caso em que a exceção não for lançada. O finally, por sua vez, funciona para os casos em que qualquer uma das duas situações ocorra. Ou seja, tendo ou não exceção, a cláusula finally será executada.

# Ela é usada, geralmente, em situações que retornem uma mensagem de finalização do programa ou que, independente do problema ocorrido, ainda possamos trabalhar com o código.

# Vejamos uma situação semelhante à anterior para aplicar esta cláusula.

# Situação 14: Você criou um código que lê um dicionário com as notas dos estudantes e quis retornar a lista de notas de um estudante. Caso o(a) estudante não esteja matriculado(a) na classe devemos tratar a exceção para aparecer a mensagem "Estudante não matriculado(a) na turma" e se a exceção não for lançada devemos exibir a lista com as notas do(a) estudante. Um texto avisando que "A consulta foi encerrada!" deve ser exibido com ou sem a exceção ser lançada. Vamos trabalhar nesse exemplo com a exceção Key Error que interromperá o processo desse pedaço do codigo. Vamos testar esse tratamento?

# Iniciaremos passando o dicionário:

notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

try:
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]
except KeyError:
    print("Estudante não matriculado(a) na turma")
else:
    print(resultado)
finally:
    print("A consulta foi encerrada!")