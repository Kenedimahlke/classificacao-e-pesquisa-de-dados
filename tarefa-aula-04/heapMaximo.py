
class HeapMaximo:
    def __init__(self, capacidade):
        self.armazenamento = [0] * capacidade
        self.capacidade = capacidade
        self.tamanho = 0

    def retorna_indice_pai(self, indice):
        return (indice - 1) // 2
    
    def retorna_indice_filho_esq(self, indice):
        return 2 * indice + 1
    
    def retorna_indice_filho_dir(self, indice):
        return 2 * indice + 2
    
    def verifica_pai(self, indice):
        return self.retorna_indice_pai(indice) >= 0
    
    def verifica_filho_esq(self, indice):
        return self.retorna_indice_filho_esq(indice) < self.tamanho
    
    def verifica_filho_dir(self, indice):
        return self.retorna_indice_filho_dir(indice) < self.tamanho
    
    def pai(self, indice):
        return self.armazenamento[self.retorna_indice_pai(indice)]
    
    def filho_esq(self, indice):
        return self.armazenamento[self.retorna_indice_filho_esq(indice)]
    
    def filho_dir(self, indice):
        return self.armazenamento[self.retorna_indice_filho_dir(indice)]
    
    def heap_cheio(self):
        return self.tamanho == self.capacidade
    
    def reorganiza(self, indice1, indice2):
        temp = self.armazenamento[indice1]
        self.armazenamento[indice1] = self.armazenamento[indice2]
        self.armazenamento[indice2] = temp

    def insere(self, valor):
        if self.heap_cheio():
            raise Exception("Heap está cheio!")
        
        self.armazenamento[self.tamanho] = valor
        self.tamanho += 1
        self.heapifyUp(self.tamanho - 1)

    def heapifyUp(self, indice):
        while self.verifica_pai(indice) and self.pai(indice) < self.armazenamento[indice]: 
            self.reorganiza(self.retorna_indice_pai(indice), indice)
            indice = self.retorna_indice_pai(indice)

    def removeMax(self): 
        if self.tamanho == 0:
            raise Exception("Heap está vazio!")
        valor = self.armazenamento[0]
        self.armazenamento[0] = self.armazenamento[self.tamanho - 1]
        self.tamanho -= 1
        self.heapifyDown(0)
        return valor
        
    def heapifyDown(self, indice):
        maior = indice  
        if self.verifica_filho_esq(indice) and self.armazenamento[maior] < self.filho_esq(indice): 
            maior = self.retorna_indice_filho_esq(indice)

        if self.verifica_filho_dir(indice) and self.armazenamento[maior] < self.filho_dir(indice):  
            maior = self.retorna_indice_filho_dir(indice)

        if maior != indice:
            self.reorganiza(indice, maior)
            self.heapifyDown(maior)
    
    def imprime(self):
        if self.tamanho == 0:
            print("Heap está vazio!")
        else:
            nivel = 0
            prox_nivel = 2 ** nivel
            for i in range(self.tamanho):
                print(self.armazenamento[i], end=" ")
                if i + 1 == prox_nivel:
                    print()
                    nivel += 1
                    prox_nivel += 2 ** nivel
            print()

heap = HeapMaximo(10)

heap.insere(15)
heap.insere(10)
heap.insere(5)
heap.insere(25)
heap.insere(35)

heap.imprime()

print("Maior elemento removido:", heap.removeMax())
heap.imprime()
