#Tabela de plano de saude

age = int(input("Type Your Age: "))

if age >= 65:
    print("$400.00")
else:
    if age >= 59:
        print("$250.00")
    else:
        if age >= 45:
            print("$150.00")
        else:
            if age >= 29:
                print("$120.00")
            else: 
                if age >= 10:
                    print("$60.00")
                else:
                    print("$30.00")