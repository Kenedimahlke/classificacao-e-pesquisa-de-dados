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

vet = [2, 7, 9, 5, 4, 3, 1, 8]

print("Vet antes de ser ordenado: ")
print(vet)

shellSort(vet)

print("Vet depois de ser ordenado: ")
print(vet)
