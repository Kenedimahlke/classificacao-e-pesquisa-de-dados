import time
import random
import sys

sys.setrecursionlimit(2000)

def insertionSort(data):
    n = len(data)
    for i in range(1, n):
        j = i - 1
        tmp = data[i]

        while(j >= 0 and tmp < data[j]):
            data[j+1] = data[j]
            j -= 1
        data[j+1] = tmp

    return data

def selectionSort(data):
    n = len(data)
    for i in range(n - 1):
        menor_id = i
        for j in range(i + 1, n):
            if data[j] < data[menor_id]:
                menor_id = j
        data[i], data[menor_id] = data[menor_id], data[i]

    return data

def bubbleSort(data):
    n = len(data)
    for i in range(n):
        for j in range(n - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
        
    return data

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

def mergeSort(v, inicio, fim):
    if inicio < fim:
        meio = (inicio + fim) // 2

        mergeSort(v, inicio, meio)
        mergeSort(v, meio + 1, fim)

        merge(v, inicio, meio, fim)

def quickSort(vet, inicio, fim):
    if inicio < fim:
        dir = partition(vet, inicio, fim)
        quickSort(vet, inicio, dir - 1)
        quickSort(vet, dir + 1, fim)

def partition(vet, inicio, fim):
    esq = inicio
    dir = fim
    pivo = vet[inicio]
    while esq < dir:
        while esq <= fim and vet[esq] <= pivo:
            esq += 1
        while dir >= 0 and vet[dir] > pivo:
            dir -= 1
        if esq < dir:
            vet[esq], vet[dir] = vet[dir], vet[esq]

    vet[inicio] = vet[dir]
    vet[dir] = pivo
    return dir

def shellSort(vet):
    n = len(vet)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = vet[i]
            j = i

            while j >= gap and vet[j - gap] > temp:
                vet[j] = vet[j - gap]
                j -= gap
            
            vet[j] = temp
        
        gap //= 2

def time_algorithm(algorithm, data):
    start_time = time.time()
    algorithm(data)
    end_time = time.time()
    return end_time - start_time

def generate_lists(n):
    ordenado = list(range(n))
    inverso = list(range(n, 0, -1))
    aleatorio = [random.randint(0, n) for _ in range(n)]
    repetidos = [random.choice(range(10)) for _ in range(n)]
    
    return ordenado, inverso, aleatorio, repetidos

def main():
    n = 1000  
    ordenado, inverso, aleatorio, repetidos = generate_lists(n)
    
    algorithms = {
        "Insertion Sort": insertionSort,
        "Selection Sort": selectionSort,
        "Bubble Sort": bubbleSort,
        "Merge Sort": lambda data: mergeSort(data, 0, len(data) - 1),
        "Quick Sort": lambda data: quickSort(data, 0, len(data) - 1),
        "Shell Sort": shellSort
    }
    
    list_types = {
        "Ordenada": ordenado,
        "Inversa": inverso,
        "Aleatória": aleatorio,
        "Repetidos": repetidos
    }
    
    for name, algorithm in algorithms.items():
        print(f"\n{name}:")
        for list_name, data in list_types.items():
            data_copy = data.copy()
            time_taken = time_algorithm(algorithm, data_copy)
            print(f"  {list_name} List: {time_taken:.6f} seconds")

if __name__ == "__main__":
    main()
