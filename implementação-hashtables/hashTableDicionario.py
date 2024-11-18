class HashTable:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = [[] for _ in range(tamanho)]

    def funcaoHash(self, key):
        return key % self.tamanho

    def inserir(self, key, valor):
        indice = self.funcaoHash(key)
        for i, (k, v) in enumerate(self.tabela[indice]):
            if k == key:
                self.tabela[indice][i] = (key, valor)
                return
        self.tabela[indice].append((key, valor))

    def busca(self, key):
        indice = self.funcaoHash(key)
        for k, v in self.tabela[indice]:
            if k == key:
                return v
        return "Key não encontrada na tabela."

    def delete(self, key):
        indice = self.funcaoHash(key)
        for i, (k, _) in enumerate(self.tabela[indice]):
            if k == key:
                del self.tabela[indice][i]
                return "Key deletada com sucesso!"
        return "Key não encontrada na tabela."


def main():
    hashTable = HashTable(10)
    hashTable.inserir(1, "Um")
    hashTable.inserir(2, "Dois")
    hashTable.inserir(3, "Três")
    hashTable.inserir(12, "Doze")  
    print("Busca da Key 2:", hashTable.busca(2))
    print("Busca da Key 12:", hashTable.busca(12))
    hashTable.delete(2)
    print("Busca da key 2 após deletar: ", hashTable.busca(2))
    print
