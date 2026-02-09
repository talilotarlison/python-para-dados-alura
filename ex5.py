notas = [ 10.0 , 5.0 , 3.0 ]

''' 
Para calcular a média de notas passadas por uma lista
lista: list, default [0]
Lista com as notas para calcular a média
return = calculo: float
Média calculada
'''

# a nossa função recebe uma lista do tipo list e retorna uma variável do tipo float
def media(lista: list) -> float:
  calculo = sum(lista) / len(lista)
  return calculo

def status_aprovacao(nota_final):
    if nota_final >= 7:
        print(f'Aprovado com sucesso. \nNotas final: {nota_final} ')
    else:
        print(f'Reprovado. \nNotas final: {nota_final} ')    

def cal_notas(notas: list)->None:
    calc = media(notas)
    status_aprovacao(calc)

cal_notas(notas= notas)



