"""6. Criar um algoritmo que leia dez números inteiros e informe o maior e o menor número.
"""
maior_numero = 0
for i in range(10):
    numero = int(input("Informe um número: "))
    if numero > maior_numero:
        maior_numero = numero
print(f"O maior número é: {maior_numero}")
