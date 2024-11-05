import math
import random

def busca_binaria_iterativa(arr, valor):
    inicio, fim = 0, len(arr) - 1
    comparacoes = 0

    while inicio <= fim:
        comparacoes += 1
        meio = (inicio + fim) // 2
        if arr[meio] == valor:
            return meio, comparacoes
        elif arr[meio] < valor:
            inicio = meio + 1
        else:
            fim = meio - 1

    return -1, comparacoes

def busca_salto(arr, valor):
    n = len(arr)
    bloco = int(math.sqrt(n))  
    passo = bloco
    anterior = 0  
    comparacoes = 0

    while anterior < n and arr[min(passo, n) - 1] < valor:
        comparacoes += 1
        anterior = passo
        passo += bloco
        if anterior >= n:
            return -1  
 
    for i in range(anterior, min(passo, n)):
        comparacoes += 1
        if arr[i] == valor:
            return i, comparacoes

    return -1, comparacoes

def busca_fibonacci(arr, valor):
    n = len(arr)
    fib_m2 = 0
    fib_m1 = 1
    fib_m = fib_m2 + fib_m1
    comparacoes = 0

    while fib_m < n:
        fib_m2 = fib_m1
        fib_m1 = fib_m
        fib_m = fib_m2 + fib_m1

    offset = -1

    while fib_m > 1:
        comparacoes += 1
        i = min(offset + fib_m2, n - 1)

        if arr[i] < valor:
            fib_m = fib_m1
            fib_m1 = fib_m2
            fib_m2 = fib_m - fib_m1
            offset = i
        elif arr[i] > valor:
            fib_m = fib_m2
            fib_m1 -= fib_m2
            fib_m2 = fib_m - fib_m1
        else:
            return i, comparacoes

    if fib_m1 and offset + 1 < n and arr[offset + 1] == valor:
        comparacoes += 1
        return offset + 1, comparacoes

    return -1, comparacoes


arr = list(range(10000))
testes = 1000  
comparacoes_binaria = comparacoes_jump = comparacoes_fibonacci = 0

for _ in range(testes):
    valor = random.choice(arr)
    _, comp_binaria = busca_binaria_iterativa(arr, valor)
    _, comp_jump = busca_salto(arr, valor)
    _, comp_fibonacci = busca_fibonacci(arr, valor)

    comparacoes_binaria += comp_binaria
    comparacoes_jump += comp_jump
    comparacoes_fibonacci += comp_fibonacci

media_binaria = comparacoes_binaria / testes
media_jump = comparacoes_jump / testes
media_fibonacci = comparacoes_fibonacci / testes

print("Média de Comparações")
print("Busca Binária:", media_binaria)
print("Pesquisa por Salto:", media_jump)
print("Pesquisa de Fibonacci:", media_fibonacci)
