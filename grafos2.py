class Grafo:
    def __init__(self):
        self.lista_adj = {}

    def inserir_vertice(self, vertice):
        if vertice not in self.lista_adj:
            self.lista_adj[vertice] = []
            print(f"Vértice '{vertice}' inserido.")
        else:
            print(f"Vértice '{vertice}' já existe.")

    def remover_vertice(self, vertice):
        if vertice in self.lista_adj:
            for v in self.lista_adj:
                if vertice in self.lista_adj[v]:
                    self.lista_adj[v].remove(vertice)
            del self.lista_adj[vertice]
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
            print(f"Aresta adicionada: {origem} → {destino}")
        else:
            print("Aresta já existe.")

    def remover_aresta(self, origem, destino):
        if origem in self.lista_adj and destino in self.lista_adj[origem]:
            self.lista_adj[origem].remove(destino)
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
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")