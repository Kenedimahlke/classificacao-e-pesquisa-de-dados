/// EASY

def selectionSort(data):
    n = len(data)
    for i in range(n -1):
        menor = data[i]
        menor_id = i

        for j in range(i +1, n):
            if data[j] < menor:
                menor = data[j]
                menor_id = j
        troca = data[i]
        data[i] = data[menor_id]
        data[menor_id] = troca

    return data

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
data3 = [1, 9, 9, 3, 3, 3, 6, 4, 7, 8, 10]
data4 = [1, 5, 3, 4, 7, 6, 8, 10, 9, 2]

print("Elementos Ordenados:\n")
print(data1)
print(selectionSort(data1))

print("\nElementos Ordenados Inversamente:\n")
print(data2)
print(selectionSort(data2))

print("\nElementos Repetidos:\n")
print(data3)
print(selectionSort(data3))

print("\nElementos Aleatórios:\n")
print(data4)
print(selectionSort(data4))
