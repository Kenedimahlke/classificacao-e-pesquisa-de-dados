import math

def busca_salto(arr, valor):
    n = len(arr)
    bloco = int(math.sqrt(n))  
    passo = bloco
    anterior = 0  

    while anterior < n and arr[min(passo, n) - 1] < valor:
        anterior = passo
        passo += bloco
        if anterior >= n:
            return -1  
 
    for i in range(anterior, min(passo, n)):
        if arr[i] == valor:
            return i

    return -1

arr = [10, 22, 35, 40, 45, 50, 80, 82, 85, 90, 100]
valor = 80

resultado_jump = busca_salto(arr, valor)
print("Índice encontrado (Jump Search):", resultado_jump)
