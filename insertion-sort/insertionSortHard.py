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

def insertionSort(lst):
    if lst is None or lst.prox is None:
        return lst  

    dummy = Lista(None)  
    dummy.prox = lst
    atual = lst

    while atual.prox:
        if atual.prox.info < atual.info:
            
            anterior = dummy
            while anterior.prox.info < atual.prox.info:
                anterior = anterior.prox

            temp = atual.prox
            atual.prox = temp.prox
            temp.prox = anterior.prox
            anterior.prox = temp
        else:
            atual = atual.prox

    return dummy.prox

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

      
        lista_ordenada = insertionSort(lista_encadeada)

   
        print(f"Data {i} ordenada: ", end="")
        while lista_ordenada:
            print(lista_ordenada.info, end=" -> ")
            lista_ordenada = lista_ordenada.prox
        print("None\n")

if __name__ == "__main__":
    main()

