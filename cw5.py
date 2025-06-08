import networkx as nx

from cw1 import graph_from_sequence
from cw2 import randomize_graph, draw


def generate_random_k_graph(n: int, k: int) -> nx.Graph:
    if n % 2 == 0 and k % 2 == 0 or n % 2 == 1 and k % 2 == 1:
        raise Exception("Illegal n and k")

    graph = graph_from_sequence([k] * n)
    return randomize_graph(graph)


def main():
    graph = generate_random_k_graph(9, 2)
    draw(graph, "cw_5")


if __name__ == "__main__":
    main()
