notas = [ 10.0 , 5.0 , 3.0 ]

def status_aprovacao(nota_final):
    if nota_final >= 7:
       return 'Aprovado'
    else:
       return 'Reprovado'

def cal_notas(notas):
    media = sum(notas)/len(notas)
    return (media, status_aprovacao(media))

boletim = cal_notas(notas)
nota , status = boletim
print(boletim, nota , status)