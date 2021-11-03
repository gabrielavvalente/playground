'''
#Exercicio 1
A = [1, 0, 5,-2,-5,7]
somaItens = A[0] + A[1] + A[5]
print(f'aqui o soma {somaItens}')
A[4] = 100

for value in A:
    print(value)

#Exercicio 2

listaDeValores = []
for index in range(6):
    listaDeValores.append(input('Digite Um Valor: '))

for value in listaDeValores:
    print(value)

#Exercicio 3

conjuntoInicial = []
conjuntoQuadrado = []

for index in range(10):
    conjuntoInicial.append(index)
    conjuntoQuadrado.append(index*index)

print(conjuntoInicial)
print(conjuntoQuadrado)

'''


