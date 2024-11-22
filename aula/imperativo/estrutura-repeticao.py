#somar numeros até limite


limite = 100
soma = 0
numero = 1

# while soma < limite:
#     soma += numero
#     numero += 1
#     print(soma)
#     print(numero)


# ENCONTRAR O PRIMEIRO NUMERO DIVISIVEL POR 7 EM UM INTERVALO
# 1 -> 99

# for numero in range (1,100) :
#     if numero % 7 ==0 :
#         print(numero)
#         break

#VERIFICAR SE TODOS OS ITENS DE UMA LISTA SÃO POSITIVOS

numeros = [1,2,3,8,9]
todos_positivos = True

for numero in numeros :
    if numero < 0 :
        print(f"esse numero é negativo {numero}")
        todos_positivos = False
        break;

if todos_positivos:
    print("Todos os números são positivos")
else:
    print("Existe número negativos")