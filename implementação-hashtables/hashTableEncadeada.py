class Node:
    def __init__(self, key, valor):
        self.key = key
        self.valor = valor
        self.proximo = None


class HashTableEncadeada:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = {i: None for i in range(tamanho)}

    def funcaoHash(self, key):
        return key % self.tamanho

    def inserir(self, key, valor):
        indice = self.funcaoHash(key)
        if self.tabela[indice] is None:
            self.tabela[indice] = Node(key, valor)
        else:
            atual = self.tabela[indice]
            while atual:
                if atual.key == key:
                    atual.valor = valor  
                    return
                if atual.proximo is None:
                    atual.proximo = Node(key, valor)
                    return
                atual = atual.proximo

    def busca(self, key):
        indice = self.funcaoHash(key)
        atual = self.tabela[indice]
        while atual:
            if atual.key == key:
                return atual.valor
            atual = atual.proximo
        return "Chave não encontrada"

    def delete(self, key):
        indice = self.funcaoHash(key)
        atual = self.tabela[indice]
        anterior = None
        while atual:
            if atual.key == key:
                if anterior is None:
                    self.tabela[indice] = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return "Chave removida com sucesso"
            anterior = atual
            atual = atual.proximo
        return "Chave não encontrada"


def main():
    hashTable = HashTableEncadeada(10)
    hashTable.inserir(1, "Um")
    hashTable.inserir(2, "Dois")
    hashTable.inserir(12, "Doze")
    print(hashTable.busca(2))  
    hashTable.delete(2)
    print(hashTable.busca(2)) 

main()
