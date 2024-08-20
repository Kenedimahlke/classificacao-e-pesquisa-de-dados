

def bubbleSort(data):
    n = len(data)
    for i in range(n):
        for j in range(n-1):
            if data[j] > data[j+1]:
                aux = data[j]
                data[j] = data[j+1]
                data[j+1] = aux
        
    return data
    
data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
data3 = [1, 9, 9, 3, 3, 3, 6, 4, 7, 8, 10]
data4 = [1, 5, 3, 4, 7, 6, 8, 10, 9, 2]

print("Elementos Ordenados:\n")
print(data1)
print(bubbleSort(data1))

print("\nElementos Ordenados Inversamente:\n")
print(data2)
print(bubbleSort(data2))

print("\nElementos Duplicados:\n")
print(data3)
print(bubbleSort(data3))

print("\nElementos Aleatórios:\n")
print(data4)
print(bubbleSort(data4))
