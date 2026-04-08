#Criar campos para inserir os numeros de indicadores e no final calcular qual a soma do card de brabos.
# media diaria de chamados 4

qtdecasos = int(input("Insira a quantidade de casos no mês: "))
diastrabalhados = int(input("Insira a quantidade de dias trabalhados no mês: "))

meta = diastrabalhados * 4

if qtdecasos >= meta:
    print("Meta batida")
else:
    print(f"Meta não batida. Faltaram {meta - qtdecasos} casos")
    
    

