def busca_binaria_iterativa(arr, valor):
    inicio = 0
    fim = len(arr) - 1

    while inicio <= fim:
        meio = (inicio + fim) // 2
        if arr[meio] == valor:
            return meio 
        elif arr[meio] < valor:
            inicio = meio + 1  
        else:
            fim = meio - 1  

    return -1  

arr = [1, 3, 5, 7, 9, 11, 13]
valor = 7

resultado_iterativa = busca_binaria_iterativa(arr, valor)
print("Índice encontrado (iterativa):", resultado_iterativa)
