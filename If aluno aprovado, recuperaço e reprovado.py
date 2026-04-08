aluno = input("Nome do aluno: ")

avaliacao1 = float(input("Nota avaliação 1: "))
avaliacao2 = float(input("Nota avaliação 2: "))
avaliacao3 = float(input("Nota avaliação 3: "))

media = (avaliacao1 + avaliacao2 + avaliacao3) / 3

print(f"A média do aluno {aluno} é {media:.2f}")  


if media >= 7:
    print("Voce foi aprovado!")
else:
    if media >=5:
        print("Vai precisar de fazer recuperação!")
    else:
        print("Voce reprovou na matéria!")