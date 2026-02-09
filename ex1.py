
notas = [ 10.0 , 5.0 , 3.0 ]

def status_aprovacao(nota_final):
    if nota_final >= 7:
        print(f'Aprovado com sucesso. \nNotas final: {nota_final} ')
    else:
        print(f'Reprovado. \nNotas final: {nota_final} ')    

def cal_notas(notas):
    soma_notas = sum(notas) 
    media = soma_notas/len(notas)
    status_aprovacao(media)

cal_notas(notas)