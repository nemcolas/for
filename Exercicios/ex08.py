""" Escreva um algoritmo que solicite o valor de N e calcule o fatorial de N."""
n = int(input("Informe o valor: "))
fatorial = 1

for i in range(1,n+1):
    fatorial = fatorial * i

print(f"O Fatorial de {n} é {fatorial}")

