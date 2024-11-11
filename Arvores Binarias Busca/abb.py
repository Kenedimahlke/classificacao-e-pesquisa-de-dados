class Node:
    def __init__(self, info):
        self.esq = None
        self.dir = None
        self.info = info

def inserir(raiz, info):
    if raiz is None:
        return Node(info)
    else: 
        if raiz.info < info:
            raiz.dir = inserir(raiz.dir, info)
        else:
            raiz.esq = inserir(raiz.esq, info)
    return raiz
    
def preOrdem(raiz):
    if raiz:
        print(raiz.info, end='')
        preOrdem(raiz.esq)
        preOrdem(raiz.dir)

def emOrdem(raiz): 
    if raiz:
        emOrdem(raiz.esq)
        print(raiz.info, end=' ')
        emOrdem(raiz.dir)

def posOrdem(raiz):
    if raiz:
        posOrdem(raiz.esq)
        posOrdem(raiz.dir)
        print(raiz.info, end=' ')

def busca(raiz, info):
    if raiz is None or raiz.info == info:
        return raiz
    if raiz.info < info:
        return busca(raiz.dir, info)
    return busca(raiz.esq, info)

def remover(raiz, info):
    if raiz is None:
        return raiz
    if info < raiz.info:
        raiz.esq = remover(raiz.esq, info)
    elif info > raiz.info:
        raiz.dir = remover(raiz.dir, info)
    else:
        if raiz.esq is None:
            return raiz.dir
        elif raiz.dir is None:
            return raiz.esq
        else:
            temp = raiz.dir
            while temp.esq is not None:
                temp = temp.esq
            raiz.info = temp.info
            raiz.dir = remover(raiz.dir, temp.info)
    return raiz

def menor_elemento(node):
    current = node
    while current.esq is not None:
         current = current.esq
    return current

def main():
    raiz = None

    # Inserção de elementos
    raiz = inserir(raiz, 10)
    raiz = inserir(raiz, 5)
    raiz = inserir(raiz, 15)
    raiz = inserir(raiz, 2)
    raiz = inserir(raiz, 12)
    raiz = inserir(raiz, 18)

    # Impressão em ordem
    print("Em Ordem:")
    emOrdem(raiz)

    # Impressão em pré-ordem
    print("\nPre-Ordem:")
    preOrdem(raiz)

    # Impressão em pós-ordem
    print("\nPós-Ordem:")
    posOrdem(raiz)

    # Busca por um elemento
    print("\nBusca por 12:")
    resultado = busca(raiz, 12)
    if resultado:
        print("Elemento encontrado:", resultado.info)
    else:
        print("Elemento não encontrado")

    # Remoção de um elemento
    print("\nRemoção de 12:")
    raiz = remover(raiz, 12)
    print("Em Ordem após remoção:")
    emOrdem(raiz)

    # Impressão em ordem após remoção
    print("\nEm Ordem após remoção:")
    emOrdem(raiz)

    # Busca por um elemento após remoção
    print("\nBusca por 12 após remoção:")
    resultado = busca(raiz, 12)
    if resultado:
        print("Elemento encontrado:", resultado.info)
    else:
        print("Elemento não encontrado")

    # Busca por um elemento que não existe
    print("\nBusca por 20:")
    resultado = busca(raiz, 20)
    if resultado:
        print("Elemento encontrado:", resultado.info)
    else:
        print("Elemento não encontrado")

    
    

