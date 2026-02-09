def media(lista: list=[0]) -> float:
    ''' Função para calcular a média de notas passadas por uma lista
    
    lista: list, default[0]
        Lista com as notas para calcular a média
        return calculo: float
        Média calculada
    '''
    
    calculo = sum(lista) / len(lista)
    
    if len(lista) > 4:
        raise ValueError("A lista não pode possuir mais de 4 notas.") # cria sua propria exceção no codigo
        
    return calculo


notas = [6, 7, 8, 8, 9]
resultado = media(notas)
print(resultado)