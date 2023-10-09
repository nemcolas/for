"""Escreva um algoritmo que leia quinze números informados pelo usuário e exiba a raiz quadrada de
cada número (Dica: utilize a biblioteca math """
import math

for i in range(15):
    numero = int(input("Informe o número: "))
    raiz = math.sqrt(numero)
    print(raiz)



