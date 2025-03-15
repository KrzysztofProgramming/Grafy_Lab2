import networkx as nx
import random
from matplotlib import pyplot as plt
from networkx import Graph

def randomize_graph(graph, iterations=500):
    for i in range(iterations):
        edges = list(graph.edges())
        edges_count = len(edges)
        edge1 = random.randrange(edges_count)
        edge2 = random.randrange(edges_count)
        if edge1 == edge2:
            continue

        (a, b) = edges[edge1]
        (c, d) = edges[edge2]

        if a != c and a != d and b != c and b != d:
            if not graph.has_edge(a, d) and not graph.has_edge(b, c):
                graph.remove_edge(a, b)
                graph.remove_edge(c, d)
                graph.add_edge(a, d)
                graph.add_edge(b, c)

    return graph


def draw(graph: Graph, name: str):
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.title(name)
    plt.savefig(name + ".png")
    plt.clf()


def main():
    degree_sequence = [5, 5, 3, 3, 2, 2, 2, 2, 2, 2]
    graph = nx.generators.degree_seq.havel_hakimi_graph(degree_sequence)
    draw(graph, "original")
    rand_graph = randomize_graph(graph, iterations=1000)
    draw(rand_graph, "random")


if __name__ == "__main__":
    main()
