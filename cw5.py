import networkx as nx

from cw2 import randomize_graph, draw


def generate_random_k_graph(n: int, k: int) -> nx.Graph:
    if n % 2 == 0 and k % 2 == 0 or n % 2 == 1 and k % 2 == 1:
        raise Exception("Illegal n and k")

    graph = nx.generators.degree_seq.havel_hakimi_graph([k] * n)
    return randomize_graph(graph)


def main():
    graph = generate_random_k_graph(9, 2)
    draw(graph, "k_generated")


if __name__ == "__main__":
    main()
