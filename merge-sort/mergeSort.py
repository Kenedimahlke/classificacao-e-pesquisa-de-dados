
def merge(v, inicio, meio, fim):
    tam = fim - inicio + 1
    temp = [0] * tam
    p1, p2 = inicio, meio + 1
    fim1, fim2 = False, False

    for i in range(tam):
        if not fim1 and not fim2:
            if v[p1] < v[p2]:
                temp[i] = v[p1]
                p1 += 1
            else:
                temp[i] = v[p2]
                p2 += 1

            if p1 > meio:
                fim1 = True
            if p2 > fim:
                fim2 = True
        else:
            if not fim1:
                temp[i] = v[p1]
                p1 += 1
            else:
                temp[i] = v[p2]
                p2 += 1

    for j in range(tam):
        v[inicio + j] = temp[j]

def mergeSort(arr, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2

        mergeSort(arr, inicio, meio)
        mergeSort(arr, meio + 1, fim)

        merge(arr, inicio, meio, fim)

def main():
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    data3 = [1, 9, 9, 3, 3, 3, 6, 4, 7, 8, 10]
    data4 = [1, 5, 3, 4, 7, 6, 8, 10, 9, 2]

    print("Lista Original: ", data1)
    mergeSort(data1, 0, len(data1) - 1)
    print("Lista Ordenada:", data1, end = "\n\n")

    print("Lista Original: ", data2)
    mergeSort(data2, 0, len(data2) - 1)
    print("Lista Ordenada:", data2, end = "\n\n")

    print("Lista Original: ", data3)
    mergeSort(data3, 0, len(data3) - 1)
    print("Lista Ordenada:", data3, end = "\n\n")

    print("Lista Original: ", data4)
    mergeSort(data4, 0, len(data4) - 1)
    print("Lista Ordenada:", data4)

main()
