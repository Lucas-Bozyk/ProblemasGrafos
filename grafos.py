class Grafo:
    def __init__(self):
        self.lista_adj = {}
        self.matriz_adj = []      
        self.vertices = []       

    def atualizar_matriz(self):
        n = len(self.vertices)
        self.matriz_adj = [[0] * n for _ in range(n)]
        for i, origem in enumerate(self.vertices):
            for destino in self.lista_adj[origem]:
                j = self.vertices.index(destino)
                self.matriz_adj[i][j] = 1

    def inserir_vertice(self, vertice):
        if vertice not in self.lista_adj:
            self.lista_adj[vertice] = []
            self.vertices.append(vertice)
            self.atualizar_matriz()
            print(f"Vértice '{vertice}' inserido.")
        else:
            print(f"Vértice '{vertice}' já existe.")

    def remover_vertice(self, vertice):
        if vertice in self.lista_adj:
            for v in self.lista_adj:
                if vertice in self.lista_adj[v]:
                    self.lista_adj[v].remove(vertice)
            del self.lista_adj[vertice]
            self.vertices.remove(vertice)
            self.atualizar_matriz()
            print(f"Vértice '{vertice}' removido.")
        else:
            print(f"Vértice '{vertice}' não existe.")

    def inserir_aresta(self, origem, destino):
        if origem not in self.lista_adj:
            self.inserir_vertice(origem)
        if destino not in self.lista_adj:
            self.inserir_vertice(destino)
        if destino not in self.lista_adj[origem]:
            self.lista_adj[origem].append(destino)
            self.atualizar_matriz()
            print(f"Aresta adicionada: {origem} → {destino}")
        else:
            print("Aresta já existe.")

    def remover_aresta(self, origem, destino):
        if origem in self.lista_adj and destino in self.lista_adj[origem]:
            self.lista_adj[origem].remove(destino)
            self.atualizar_matriz()
            print(f"Aresta removida: {origem} → {destino}")
        else:
            print("Aresta não existe.")

    def mostrar_grau(self):
        print("\nGrau de cada vértice:")
        for vertice in self.lista_adj:
            grau = len(self.lista_adj[vertice])
            print(f"Vértice {vertice}: grau = {grau}")

    def existe_aresta(self, origem, destino):
        if origem in self.lista_adj and destino in self.lista_adj[origem]:
            print(f"Existe uma aresta de {origem} para {destino}.")
            return True
        print(f"Não existe aresta de {origem} para {destino}.")
        return False

    def listar_vizinhos(self, vertice):
        if vertice in self.lista_adj:
            print(f"Vizinhos de {vertice}: {self.lista_adj[vertice]}")
            return self.lista_adj[vertice]
        else:
            print("Vértice não encontrado.")
            return []

    def verificar_percurso(self, percurso):
        for i in range(len(percurso) - 1):
            origem = percurso[i]
            destino = percurso[i + 1]
            if origem not in self.lista_adj or destino not in self.lista_adj[origem]:
                print(f"Percurso inválido: não existe aresta de {origem} para {destino}.")
                return False
        print("Percurso é possível!")
        return True

    def mostrar_grafo(self):
        print("\nLista de Adjacência:")
        for vertice, vizinhos in self.lista_adj.items():
            print(f"{vertice} → {vizinhos}")

        print("\nMatriz de Adjacência:")
        print("   " + "  ".join(self.vertices))
        for i, v in enumerate(self.vertices):
            linha = "  ".join(map(str, self.matriz_adj[i]))
            print(f"{v}: {linha}")


if __name__ == "__main__":
    g = Grafo()

    g.inserir_vertice("A")
    g.inserir_vertice("B")
    g.inserir_vertice("C")

    g.inserir_aresta("A", "B")
    g.inserir_aresta("A", "C")
    g.inserir_aresta("B", "C")

    g.mostrar_grafo()
    g.mostrar_grau()
    g.existe_aresta("A", "B")
    g.listar_vizinhos("A")

    percurso = ["A", "B", "C"]
    g.verificar_percurso(percurso)

    g.remover_aresta("A", "C")
    g.remover_vertice("B")

    g.mostrar_grafo()

print("Try programiz.pro")
