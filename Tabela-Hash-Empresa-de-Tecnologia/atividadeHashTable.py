class Node:
    def __init__(self, nome, caminho, tamanho):
        self.nome = nome
        self.caminho = caminho
        self.tamanho = tamanho
        self.proximo = None

    def __str__(self):
        return f"Nome: {self.nome}, Caminho: {self.caminho}, Tamanho: {self.tamanho} KB"


class HashTableArquivos:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabela = {i: None for i in range(tamanho)}

    def funcaoHash(self, nome):
        return sum(ord(c) for c in nome) % self.tamanho

    def inserir(self, nome, caminho, tamanho):
        indice = self.funcaoHash(nome)
        novo_node = Node(nome, caminho, tamanho)
        if self.tabela[indice] is None:
            self.tabela[indice] = novo_node
        else:
            atual = self.tabela[indice]
            while atual:
                if atual.nome == nome:
                    atual.caminho = caminho
                    atual.tamanho = tamanho
                    return "Arquivo atualizado com sucesso."
                if atual.proximo is None:
                    break
                atual = atual.proximo
            atual.proximo = novo_node

    def buscar(self, nome):
        indice = self.funcaoHash(nome)
        atual = self.tabela[indice]
        while atual:
            if atual.nome == nome:
                return str(atual)
            atual = atual.proximo
        return "Arquivo não encontrado."

    def remover(self, nome):
        indice = self.funcaoHash(nome)
        atual = self.tabela[indice]
        anterior = None
        while atual:
            if atual.nome == nome:
                if anterior is None:
                    self.tabela[indice] = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                return "Arquivo removido com sucesso."
            anterior = atual
            atual = atual.proximo
        return "Arquivo não encontrado."

    def listar(self):
        arquivos = []
        for indice in range(self.tamanho):
            atual = self.tabela[indice]
            while atual:
                arquivos.append(str(atual))
                atual = atual.proximo
        return arquivos if arquivos else ["Nenhum arquivo armazenado."]

tabela = HashTableArquivos(10)

tabela.inserir("relatorio.pdf", "/documentos/relatorio.pdf", 1024)
tabela.inserir("foto.jpg", "/imagens/foto.jpg", 2048)
tabela.inserir("dados.csv", "/planilhas/dados.csv", 512)
tabela.inserir("backup.zip", "/backup/backup.zip", 4096)
tabela.inserir( "arquivo.txt", "/arquivos/arquivo.txt", 3072)
tabela.inserir("video.mp4", "/videos/video.mp4", 8192)
tabela.inserir("musica.mp3", "/musicas/musica.mp3", 1024)
tabela.inserir("livro.pdf", "/livros/livro.pdf", 2048)
tabela.inserir("aplicacao.exe", "/aplicacoes/aplicacao.exe", 512)
tabela.inserir("software.iso", "/software/software.iso", 1024)

print(tabela.buscar("dados.csv"))

print(tabela.remover("foto.jpg"))  

print("\n".join(tabela.listar()))  
