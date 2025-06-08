import matplotlib.pyplot as plt
import numpy as np
import networkx as nx

from cw1 import graph_from_sequence


class Task3:
    def __init__(self):
        self.graph = nx.Graph()

    def visualize_connected_components(self, components=None, title="Spójne składowe", name="cw_3"):
        plt.figure(figsize=(6, 6))
        x0, y0, r = 0, 0, 5
        alpha = 2 * np.pi / len(self.graph.edges)
        positions = {i: (x0 + r * np.cos(i * alpha), y0 + r * np.sin(i * alpha)) for i in self.graph.nodes}

        circle = plt.Circle((x0, y0), r, color='black', fill=False, linestyle='dashed')
        plt.gca().add_patch(circle)

        components = components if components else self.find_connected_components()
        colors = ["red", "blue", "green", "purple", "orange", "cyan", "magenta", "yellow"]
        color_map = {}

        for idx, component in enumerate(components):
            color = colors[idx % len(colors)]
            for node in component:
                color_map[node] = color

        for u, v in self.graph.edges:
            x_values = [positions[u][0], positions[v][0]]
            y_values = [positions[u][1], positions[v][1]]
            plt.plot(x_values, y_values, 'gray')

        for i, (x, y) in positions.items():
            plt.scatter(x, y, color=color_map[i], edgecolors='black', s=300)
            plt.text(x, y, str(i), fontsize=12, ha='center', va='center')

        plt.axis('off')
        plt.xlim(x0 - r - 1, x0 + r + 1)
        plt.ylim(y0 - r - 1, y0 + r + 1)

        plt.title(title)
        plt.savefig(name + ".png")

    def find_connected_components(self):
        def dfs(v, component_id, component):
            comp[v] = component_id
            component.append(v)
            for neighbor in self.graph.neighbors(v):
                if comp[neighbor] == -1:
                    dfs(neighbor, component_id, component)

        comp = {v: -1 for v in self.graph.nodes}
        components = []
        component_id = 0

        # dla każdego node'a przechodzimy DFSem i po drodze dodajemy go do odwiedzonych nadając id
        # po każdym cylku DFSa zwiększamy globalny licznik id
        for v in self.graph.nodes:
            if comp[v] == -1:
                component_id += 1
                component = []
                dfs(v, component_id, component)
                components.append(component)

        # opcjonalnie dla wyświetlania
        components.sort(key=len, reverse=True)
        return components


def test_task3():
    degree_sequence = [4, 2, 2, 3, 2, 1, 4, 2, 2, 2, 2]
    task3 = Task3()
    task3.graph = graph_from_sequence(degree_sequence)

    components = task3.find_connected_components()
    for idx, component in enumerate(components, start=1):
        print(f"{idx})", " ".join(map(str, component)))

    print(f"Największa składowa ma numer {1 if components else 'brak'}.")

    task3.visualize_connected_components(components)


if __name__ == "__main__":
    test_task3()
