/// HARD


class Lista:
    def __init__(self, info=None):
        self.info = info
        self.prox = None

def insere_na_lista(lst, valor):
    novo_no = Lista(valor)
    if lst is None:
        return novo_no
    else:
        ultimo = lst
        while ultimo.prox:
            ultimo = ultimo.prox
        ultimo.prox = novo_no
    return lst

def selectionSort(lst):
    if lst is None or lst.prox is None:
        return lst

    inicio = lst

    while inicio is not None:

        menor = inicio
        atual = inicio.prox

        while atual is not None:
            if atual.info < menor.info:
                menor = atual
            atual = atual.prox

        inicio.info, menor.info = menor.info, inicio.info

        inicio = inicio.prox

    return lst

def main():
    data1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    data2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    data3 = [1, 9, 9, 3, 3, 3, 6, 4, 7, 8, 10]
    data4 = [1, 5, 3, 4, 7, 6, 8, 10, 9, 2]
    
    datasets = [data1, data2, data3, data4]
    
    for i, data in enumerate(datasets, 1):
        print(f"Data {i} original: {data}")

        lista_encadeada = None
        for val in data:
            lista_encadeada = insere_na_lista(lista_encadeada, val)

        lista_ordenada = selectionSort(lista_encadeada)

        print(f"Data {i} ordenada: ", end="")
        while lista_ordenada:
            print(lista_ordenada.info, end=" -> ")
            lista_ordenada = lista_ordenada.prox
        print("None\n")

if __name__ == "__main__":
    main()
