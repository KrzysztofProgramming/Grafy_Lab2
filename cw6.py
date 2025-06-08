import networkx as nx
from networkx import Graph
import matplotlib.pyplot as plt

from cw1 import graph_from_sequence


def find_hamilton_cycle(graph: Graph) -> list[int]:
    nodes_len = graph.number_of_nodes()
    nodes = list(graph.nodes())

    def dfs(current_node, visited, path) -> list[int]:
        path.append(current_node)
        if len(path) == nodes_len and path[0] in graph.neighbors(current_node):
            return path

        for neighbor in graph.neighbors(current_node):
            if neighbor not in visited:
                visited.append(neighbor)
                result = dfs(neighbor, visited, path)
                if result:
                    return result
                visited.pop()

        path.pop()
        return []

    for start_node in nodes:
        start_path = []
        visited_nodes = [start_node]
        return dfs(start_node, visited_nodes, start_path)

    return []


def draw_hamiltonian_graph(graph: Graph, cycle: list[int]):
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos, with_labels=True, node_color='lightblue')
    cycle_edges = [(cycle[i], cycle[i + 1]) for i in range(len(cycle) - 1)]
    cycle_edges.append((cycle[-1], cycle[0]))
    nx.draw_networkx_edges(graph, pos, edgelist=cycle_edges, edge_color='red', width=2)
    plt.show()


def main():
    # seq = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    seq = [6, 6, 6, 6, 6, 6, 6, 6, 4, 4, 4]
    graph = graph_from_sequence(seq)

    cycle = find_hamilton_cycle(graph)
    if cycle:
        print("Znaleziono cykl Hamiltona:", cycle)
        draw_hamiltonian_graph(graph, cycle)
    else:
        print("Graf nie jest Hamiltonowski.")


if __name__ == "__main__":
    main()
