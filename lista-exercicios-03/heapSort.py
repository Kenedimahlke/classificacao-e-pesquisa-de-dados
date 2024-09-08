
def heapify(vet, n, i):
    maior = i
    filho_esq = 2 * i + 1
    filho_dir = 2 * i + 2

    if filho_esq < n and vet[filho_esq] > vet[maior]:
        maior = filho_esq

    if filho_dir < n and vet[filho_dir] > vet[maior]:
        maior = filho_dir

    if maior != i:
        vet[i], vet[maior] = vet[maior], vet[i]
        heapify(vet, n, maior)


def heapSort(vet):
    n = len(vet)

    for i in range(n // 2 - 1, -1, -1):
        heapify(vet, n, i)

    for i in range(n - 1, 0, -1):
        vet[i], vet[0] = vet[0], vet[i]
        heapify(vet, i, 0)


vet = [1, 7, 4, 19, 20, 43, 3, 10, 11, 8, 6]
heapSort(vet)
print("Lista Ordenada: ")
print(vet)
