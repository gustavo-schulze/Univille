#Problema do Caixeiro Viajante resolvido por Força Bruta

import itertools
import time


# Exemplo 1: 4 cidades, todas ligadas entre si (cidade_a, cidade_b, custo)
ARESTAS_EXEMPLO_PEQUENO = [
    ("A", "B", 10), ("A", "C", 15), ("A", "D", 20),
    ("B", "C", 35), ("B", "D", 25),
    ("C", "D", 30),
]

# Exemplo 2: grafo da atividade (10 cidades e 17 estradas)
ARESTAS_MAPA = [
    (9, 10, 12), (9, 8, 10), (9, 7, 21),
    (10, 2, 11), (10, 8, 8),
    (2, 4, 12), (2, 1, 8), (2, 3, 9),
    (4, 5, 19),
    (1, 8, 8), (1, 3, 13), (1, 6, 14),
    (8, 6, 18),
    (3, 6, 15), (3, 5, 13),
    (7, 6, 22),
    (6, 5, 15),
]


# Monta o grafo como dicionário cidade -> {vizinha: custo}; as estradas valem nos dois sentidos
def montar_grafo(arestas):
    grafo = {}
    for origem, destino, custo in arestas:
        grafo.setdefault(origem, {})[destino] = custo
        grafo.setdefault(destino, {})[origem] = custo
    return grafo


# Soma o custo de uma rota; retorna None se algum trecho não tiver estrada direta
def custo_da_rota(grafo, rota):
    total = 0
    for atual, proxima in zip(rota, rota[1:]):
        if proxima not in grafo[atual]:
            return None
        total += grafo[atual][proxima]
    return total


# Testa todas as permutações das demais cidades (a inicial fica fixa) e guarda a mais barata
def caixeiro_forca_bruta(grafo, cidade_inicial):
    outras = sorted(cidade for cidade in grafo if cidade != cidade_inicial)
    melhor_rota = None
    melhor_custo = float("inf")
    testadas = 0
    validas = []  # lista de (rota, custo) das permutações que formam um ciclo existente

    for permutacao in itertools.permutations(outras):
        testadas += 1
        rota = (cidade_inicial,) + permutacao + (cidade_inicial,)
        custo = custo_da_rota(grafo, rota)
        if custo is None:
            continue
        validas.append((rota, custo))
        if custo < melhor_custo:
            melhor_custo = custo
            melhor_rota = rota

    return melhor_rota, melhor_custo, testadas, validas


# Converte uma rota em texto no formato 1 -> 2 -> 3
def formatar_rota(rota):
    return " -> ".join(str(cidade) for cidade in rota)


# Executa a força bruta para um conjunto de arestas e imprime entrada, execução e resposta
def resolver(titulo, arestas, cidade_inicial):
    grafo = montar_grafo(arestas)
    print(f"===== {titulo} =====")
    print(f"Cidades: {len(grafo)} | Estradas: {len(arestas)} | Cidade inicial: {cidade_inicial}")

    inicio = time.perf_counter()
    melhor_rota, melhor_custo, testadas, validas = caixeiro_forca_bruta(grafo, cidade_inicial)
    duracao = time.perf_counter() - inicio

    print(f"Permutações testadas: {testadas}")
    print(f"Rotas válidas (todas as estradas existem): {len(validas)}")
    for rota, custo in validas:
        marcador = "  <- menor custo" if custo == melhor_custo else ""
        print(f"  {formatar_rota(rota)} = {custo}{marcador}")

    if melhor_rota is None:
        print("Não existe rota que visite todas as cidades e volte à inicial.\n")
        return

    print(f"Melhor rota: {formatar_rota(melhor_rota)}")
    print(f"Custo total: {melhor_custo}")
    print(f"Tempo de execução: {duracao:.3f} s\n")


def main():
    resolver("EXEMPLO 1 - 4 CIDADES", ARESTAS_EXEMPLO_PEQUENO, "A")
    resolver("EXEMPLO 2 - GRAFO DA ATIVIDADE", ARESTAS_MAPA, 1)


if __name__ == "__main__":
    main()
