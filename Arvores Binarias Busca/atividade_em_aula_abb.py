class Node:
    def __init__(self, id, nome=None, descricao=None, preco=None):
        self.esq = None
        self.dir = None
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco

def inserir(raiz, id, nome, descricao, preco):
    if raiz is None:
        return Node(id, nome, descricao, preco)
    else:
        if id < raiz.id:
            raiz.esq = inserir(raiz.esq, id, nome, descricao, preco)
        else:
            raiz.dir = inserir(raiz.dir, id, nome, descricao, preco)
    return raiz

def remover(raiz, id):
    if raiz is None:
        return raiz
    if id < raiz.id:
        raiz.esq = remover(raiz.esq, id)
    elif id > raiz.id:
        raiz.dir = remover(raiz.dir, id)
    else:
        if raiz.esq is None:
            return raiz.dir
        elif raiz.dir is None:
            return raiz.esq
        temp = raiz.dir
        while temp.esq is not None:
            temp = temp.esq
        raiz.id = temp.id
        raiz.nome = temp.nome
        raiz.descricao = temp.descricao
        raiz.preco = temp.preco
        raiz.dir = remover(raiz.dir, temp.id)
    return raiz

def buscar(raiz, id):
    if raiz is None or raiz.id == id:
        return raiz
    if id < raiz.id:
        return buscar(raiz.esq, id)
    return buscar(raiz.dir, id)

def listar_em_ordem(raiz):
    if raiz:
        listar_em_ordem(raiz.esq)
        print(f'ID: {raiz.id}, Nome: {raiz.nome}, Descrição: {raiz.descricao}, Preço: {raiz.preco}')
        listar_em_ordem(raiz.dir)

def main():
    # Criando a raiz da árvore
    raiz = None

    # Inserindo produtos
    raiz = inserir(raiz, 30, "Produto 1", "Descrição 1", 100.0)
    raiz = inserir(raiz, 20, "Produto 2", "Descrição 2", 200.0)
    raiz = inserir(raiz, 40, "Produto 3", "Descrição 3", 300.0)

    # Listando produtos em ordem crescente de ID
    print("Lista de produtos em ordem crescente de ID:")
    listar_em_ordem(raiz)

    # Buscando produto com ID 20
    print("\nBuscando produto com ID 20:")
    produto = buscar(raiz, 20)
    if produto:
        print(f'Encontrado - ID: {produto.id}, Nome: {produto.nome}, Descrição: {produto.descricao}, Preço: {produto.preco}')
    else:
        print("Produto não encontrado.")

    # Deletando produto com ID 20
    print("\nDeletando produto com ID 20.")
    raiz = remover(raiz, 20)

    # Listando produtos em ordem crescente de ID após deletado
    print("\nLista de produtos em ordem crescente de ID após deletado:")
    listar_em_ordem(raiz)

if __name__ == "__main__":
    main()
