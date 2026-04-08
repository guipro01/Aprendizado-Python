#Calculo de notas

nome = input("Digite o nome do aluno: ")

if nome.isdigit():
    print("Seu nome não pode ser numero!")
    
avaliacao1 = float(input("Avaliação 1:"))
while avaliacao1 < 0 or avaliacao1 > 10:
    print("Nota invalida!")
    avaliacao1 = float(input("Avaliação 1:"))

avaliacao2 = float(input("avaliação 2:"))
while avaliacao2 < 0 or avaliacao2 > 10:
    print("Nota invalida!")
    avaliacao2 = float(input("Avaliação 2:"))
    
avaliacao3 = float(input("Avaliação 3:"))    
while avaliacao3 < 0 or avaliacao3 > 10:
    print("Nota invalida!")    
    avaliacao3 = float(input("Avaliação 3:"))
    
media = (avaliacao1 + avaliacao2 + avaliacao3) /3

if media >=7:
    print(f"{nome} Sua média foi {media:.3f}! Status: Aprovado!")
else:
    if media >=5:
        print(f"{nome} Sua média foi {media:.3f}! Status: Está de recuperação!")
    else:
        print(f"{nome} Sua média foi {media:.3f}! Status: Foi reprovado!")


