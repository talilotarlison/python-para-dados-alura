# Ao longo deste curso, observamos alguns erros nas execuções dos nossos códigos. Você, como pessoa programadora ou cientista de dados, precisa estar atenta ou atento aos erros que podem surgir durante a execução do programa, pois eles podem atrapalhar a experiência do usuário, impedindo que algumas análises sejam feitas de maneira correta.

# As exceções são erros que ocorrem dentro a execução do programa e interrompem o fluxo do programa quando não tratadas. Para isso, precisamos saber identificar esses erros e tratá-los.

# Nesta documentação do Python, falamos sobre erros e exceções. Mas há, também, uma atividade que explica alguns desses erros que podem ser identificados no nosso programa.

# Seguindo para o tratamento de exceções, pensemos o seguinte: você solicita à pessoa usuária que ela coloque um valor. Porém, ela digita uma entrada inválida que, se não tratada ou entendida pelo código, pode interromper o curso do programa. Sendo assim, quando tratamos uma exceção, tentamos criar fluxos alternativos para que o código não deixe de responder àquela pessoa usuária que aquele tipo de dado não é bem recebido ou precisa ser digitado novamente. Criaremos, então, um fluxo alternativo.

# Imagine que temos um código com um fluxo padrão a este código. Caso alguma exceção ou erro ocorra, ao invés de quebrarmos este fluxo padrão, entramos em um fluxo alternativo, no caso, uma exceção, que gera para o usuário uma explicação do erro ou um caminho alternativo para seguir na execução do programa.

# Explicaremos o tratamento de exceções a partir de algumas cláusulas, começando pela Try...Except.

# Try...Except
# Nela, temos dois tipos de cláusulas em que try representa o código padrão. Caso não ocorra nenhuma exceção, ele será executado por completo e o programa seguirá.

# Se uma exceção for lançada, quebramos a execução de try e continuamos com o que precisa ser executado em except, que seria a cláusula de exceção. Ou seja, a cláusula except só será acionada se uma exceção for lançada na cláusula try.

# Esta exceção não precisa necessariamente ser declarada, então podemos apenas incluir except e as instruções de código. Caso optemos por declarar o nome da exceção, o passamos seguido d o apelido e.

notas = {'João': [8.0, 9.0, 10.0], 'Maria': [9.0, 7.0, 6.0], 'José': [3.4, 7.0, 8.0],'Cláudia': [5.5, 6.6, 8.0], 'Ana': [6.0, 10.0, 9.5], 'Joaquim': [5.5, 7.5, 9.0], 'Júlia': [6.0, 8.0, 7.0], 'Pedro': [3.0, 4.0, 6.0]}

try:
    nome = input("Digite o nome do(a) estudante: ")
    resultado = notas[nome]
except Exception as e:
    print(type(e), f"Erro: {e}")