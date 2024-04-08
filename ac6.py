"""
Programação Estruturada
AC6
Marcelle Lohane
"""
#Exercicio 1 

print("Hello World!")

# Exercício 2 

a = int(input())
b = int(input())

x = a + b

print(f"X = {x}")

# Exercicio 3

codigo1, unidades1, preco1 = map(float, input().split())
codigo2, unidades2, preco2 = map(float, input().split())

total_pagar = (unidades1 * preco1) + (unidades2 * preco2)

print("VALOR A PAGAR: R$ {:.2f}".format(total_pagar))

#Exercicio 4

valores = input().split()

valores = [int(x) for x in valores]

maior = max(valores)


print(maior, "eh o maior")

#Exercicio 5 

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())


distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

print("{:.4f}".format(distancia))
