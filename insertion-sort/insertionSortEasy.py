///EASY

def insertionSort(data):
    n = len(data)
    j = 1
    for i in range (j, n):
        j = i- 1
        tmp = data[i]

        while(j >= 0 and tmp < data[j]):
            data[j+1] = data[j]
            j-=1
        data[j+1] = tmp

    return data

data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
data3 = [1, 9, 9, 3, 3, 3, 6, 4, 7, 8, 10]
data4 = [1, 5, 3, 4, 7, 6, 8, 10, 9, 2]

print("Elementos Ordenados:\n")
print(data1)
print(insertionSort(data1))

print("\nElementos Ordenados Inversamente:\n")
print(data2)
print(insertionSort(data2))

print("\nElementos Repetidos:\n")
print(data3)
print(insertionSort(data3))

print("\nElementos Aleatórios:\n")
print(data4)
print(insertionSort(data4))
