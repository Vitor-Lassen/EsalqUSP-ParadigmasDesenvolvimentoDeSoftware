#Recursão
# fatorial 
def fatorial(num ):
    if num <= 1:
        return num
    return num * fatorial(num -1)

print(fatorial(4))

#fibonachi 


def fibo(num):
    if num == 0 : return 0
    if num == 1 : return 1
    return fibo(num - 2) + fibo(num - 1)

print(fibo(6))
