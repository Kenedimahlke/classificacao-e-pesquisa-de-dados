def quickSort(vet, inicio, fim):
     if(fim > inicio):
          pivo = particiona(vet, inicio, fim)
          quickSort(vet, inicio, pivo -1)
          quickSort(vet, pivo +1, fim)
          
def particiona(vet, inicio, fim):
    esq = inicio
    dir = fim 
    pivo = vet[inicio]

    while(esq < dir):
        while(esq <= fim and vet[esq] <= pivo):
             esq += 1   

        while(dir >= 0 and vet[dir] > pivo):
             dir -= 1

        if(esq < dir):
             vet[esq], vet[dir] = vet[dir], vet[esq]


    vet[inicio] = vet[dir]
    vet[dir] = pivo
    return dir


def main():
    vet = [5, 3, 8, 1, 2, 7, 4, 6]
    quickSort(vet, 0, len(vet)-1)
    print(vet)

main()
