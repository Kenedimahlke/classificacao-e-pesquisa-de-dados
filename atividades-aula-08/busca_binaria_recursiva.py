def busca_binaria_recursiva(arr, valor, inicio, fim):
    if inicio > fim:
        return -1  

    meio = (inicio + fim) // 2

    if arr[meio] == valor:
        return meio  
    elif arr[meio] < valor:
        return busca_binaria_recursiva(arr, valor, meio + 1, fim)  
    else:
        return busca_binaria_recursiva(arr, valor, inicio, meio - 1)  

arr = [1, 3, 5, 7, 9, 11, 13]
valor = 7

resultado_recursiva = busca_binaria_recursiva(arr, valor, 0, len(arr) - 1)
print("Índice encontrado (recursiva):", resultado_recursiva)
