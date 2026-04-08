

#Perguntas de investigação!

pergunta1 = input("Telefonou para a vitima? ").lower()
pergunta2 = input("Esteve no local do crime? ").lower()
pergunta3 = input("Mora perto da vítima? ").lower()
pergunta4 = input("Devia para vítima? ").lower()
pergunta5 = input("Já trabalhou com a vítima? ").lower()

contagem = 0 

if pergunta1 == "sim":
    contagem += 1
if pergunta2 == "sim":
    contagem += 1
if pergunta3 =="sim":
    contagem += 1
if pergunta4 == "sim":
    contagem += 1
if pergunta5 =="sim":
    contagem += 1
    
    
if contagem == 5:
    print("Assasino!")
else:
    if contagem >= 3:
        print("Cumplice, prenda-o!!")
    else:
        if contagem >=2:
            print("Suspeito!")
        else: 
            print("Inocente")
    
    