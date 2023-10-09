conta_pares = 0 #Contando o número de pares com For

for i in range (10):
    numero = int(input("Informe o número: "))
    if numero % 2 == 0:
        conta_pares +=1

print(f"Quantidade de pares: {conta_pares}")
