def lernotas():
    n=float(input("digite uma nota para o aluno(a): "))
    return n


def resultado(n1, n2):
    media=(n1+n2)/2
    print("nota A : ", n1)
    print("nota B : ", n2)
    print("Media: ", media, "Resultado: ", end="")
    if media >= 7 :
        print("Aprovado")
    else:
        print("Reprovado")


a = lernotas()
b = lernotas()
resultado(a, b)