def criar_grafo():

    return [], []


def inserir_vertice(vertices, arestas, vertice):
    if vertice not in vertices:
        vertices.append(vertice)
        print(f"Vértice '{vertice}' adicionado com sucesso.")
    else:
        print(f"Vértice '{vertice}' já existe.")


def remover_vertice(vertices, arestas, vertice):
    if vertice in vertices:
        vertices.remove(vertice)
        arestas[:] = [a for a in arestas if vertice not in a]
        print(f"Vértice '{vertice}' e suas arestas foram removidos.")
    else:
        print(f"Vértice '{vertice}' não encontrado.")


def inserir_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if origem not in vertices:
        vertices.append(origem)
    if destino not in vertices:
        vertices.append(destino)

    if (origem, destino) not in arestas:
        arestas.append((origem, destino))
        print(f"Aresta {origem} -> {destino} adicionada.")
    else:
        print("Aresta já existe.")

    if nao_direcionado and (destino, origem) not in arestas:
        arestas.append((destino, origem))
        print(f"Aresta {destino} -> {origem} adicionada (não direcionado).")


def remover_aresta(vertices, arestas, origem, destino, nao_direcionado=False):
    if (origem, destino) in arestas:
        arestas.remove((origem, destino))
        print(f"Aresta {origem} -> {destino} removida.")
    else:
        print("Aresta não encontrada.")

    if nao_direcionado and (destino, origem) in arestas:
        arestas.remove((destino, origem))
        print(f"Aresta {destino} -> {origem} removida (não direcionado).")


def existe_aresta(vertices, arestas, origem, destino):
    return (origem, destino) in arestas


def vizinhos(vertices, arestas, vertice):
    if vertice not in vertices:
        print(f"Vértice '{vertice}' não existe.")
        return []
    return [dest for (orig, dest) in arestas if orig == vertice]


def grau_vertices(vertices, arestas, nao_direcionado=False):
    graus = {}
    for v in vertices:
        saida = len([1 for (orig, dest) in arestas if orig == v])
        entrada = len([1 for (orig, dest) in arestas if dest == v])
        if nao_direcionado:
            graus[v] = saida + entrada
        else:
            graus[v] = {"saida": saida, "entrada": entrada, "total": saida + entrada}
    return graus


def percurso_valido(vertices, arestas, caminho):
    for i in range(len(caminho) - 1):
        if not existe_aresta(vertices, arestas, caminho[i], caminho[i + 1]):
            return False
    return True


def listar_vizinhos(vertices, arestas, vertice):
    viz = vizinhos(vertices, arestas, vertice)
    print(f"Vizinhos de {vertice}: {viz}")
    return viz


def exibir_grafo(vertices, arestas):
    print("\n--- GRAFO (Lista de Arestas) ---")
    print("Vértices:", vertices)
    print("Arestas:")
    for (o, d) in arestas:
        print(f"  {o} -> {d}")
    print("-------------------------------\n")


def main():
    vertices, arestas = criar_grafo()

    while True:
        print("""
==================== MENU ====================
1 - Inserir vértice
2 - Remover vértice
3 - Inserir aresta
4 - Remover aresta
5 - Exibir grafo
6 - Calcular grau dos vértices
7 - Verificar existência de aresta
8 - Listar vizinhos de um vértice
9 - Verificar percurso válido
0 - Sair
==============================================
        """)

        opc = input("Escolha uma opção: ")

        if opc == "1":
            v = input("Digite o nome do vértice: ")
            inserir_vertice(vertices, arestas, v)

        elif opc == "2":
            v = input("Digite o vértice a remover: ")
            remover_vertice(vertices, arestas, v)

        elif opc == "3":
            o = input("Vértice de origem: ")
            d = input("Vértice de destino: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            inserir_aresta(vertices, arestas, o, d, nd)

        elif opc == "4":
            o = input("Origem da aresta: ")
            d = input("Destino da aresta: ")
            nd = input("É não direcionado? (s/n): ").lower() == "s"
            remover_aresta(vertices, arestas, o, d, nd)

        elif opc == "5":
            exibir_grafo(vertices, arestas)

        elif opc == "6":
            nd = input("Grafo é não direcionado? (s/n): ").lower() == "s"
            graus = grau_vertices(vertices, arestas, nd)
            for v, g in graus.items():
                print(f"{v}: {g}")

        elif opc == "7":
            o = input("Origem: ")
            d = input("Destino: ")
            print("Existe aresta?", existe_aresta(vertices, arestas, o, d))

        elif opc == "8":
            v = input("Digite o vértice: ")
            listar_vizinhos(vertices, arestas, v)

        elif opc == "9":
            caminho = input("Digite o percurso (ex: A-B-C): ").split("-")
            print("Percurso válido?", percurso_valido(vertices, arestas, caminho))

        elif opc == "0":
            print("Encerrando programa...")
            break

        else:
            print("Opção inválida! Tente novamente.")


if __name__ == "__main__":
    main()
