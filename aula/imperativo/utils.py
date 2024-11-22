def calcular_media(notas):
    soma = 0
    qtd = 0

    for nota in notas:
        soma += nota
        qtd += 1
    media = soma/qtd
    return media

def classicar_aluno(notas):
    media = calcular_media(notas)

    if media >= 7 :
        return "Aprovado"
    elif media >= 5 : 
        return "Recuperação"
    else: 
        return "Reprovado"