def countingSort(vet):
    if not vet:
        return vet
    
    max_val = max(vet)
    min_val = min(vet)
    count_range = max_val - min_val + 1
    count = [0] * count_range

    for num in vet:
        count[num - min_val] += 1

    sorted_index = 0
    for i in range(count_range):
        while count[i] > 0:
            vet[sorted_index] = i + min_val
            sorted_index += 1
            count[i] -= 1

    return vet

vet = [4, 2, 2, 8, 3, 3, 1]
sorted_vet = countingSort(vet)
print("Vetor ordenado:", sorted_vet)
