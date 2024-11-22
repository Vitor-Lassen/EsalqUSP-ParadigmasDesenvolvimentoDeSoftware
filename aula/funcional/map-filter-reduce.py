from functools import reduce

numeros = [1,2,3,4,5,6,7,8,9,10]

#map, filter, reduce 

#Filtrar os Números pares 

numeros_pares = list(filter(lambda x : x%2 ==0, numeros))
print(numeros_pares)

numeros_pares_dobrados = list(map(lambda x:x*2, numeros_pares))
print(numeros_pares_dobrados)


soma_numeros_pares_dobrados = reduce(lambda x, y: x+y, numeros_pares_dobrados)

print(soma_numeros_pares_dobrados)