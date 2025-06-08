import matplotlib.pyplot as plt
import networkx as nx

    
def is_graphical_sequence(sequence):
    seq=sequence.copy()
    if sum(seq) % 2 != 0:
        return False
    
    seq.sort(reverse=True)
    while True:
        if seq[-1]<0:
            return False
        
        first=seq[0]
        if first>=len(seq):
            return False
        
        if first==0:
            return True
        
        seq.pop(0)
        for i in range(first):
            seq[i]-=1
        seq.sort(reverse=True)


def graph_from_sequence(seq):
    degrees=seq.copy()
    if not is_graphical_sequence(degrees):
        print("Given sequence is not a graphical sequence.")
        return None
    
    graph = nx.Graph()
    n = len(degrees)
    nodes = list(range(n))
    graph.add_nodes_from(nodes)
    
    degrees.sort(reverse=True)
    # zamieniamy do postaci: [[0, 4], [1, 4], [2, 3], ...]
    indexed_degrees =  [[i, degrees[i]] for i in range(n)]
    # jeżeli stopień jest większy od 0 to dodajemy krawędzie
    while indexed_degrees[0][1]>0:
        max_node, max_degree = indexed_degrees.pop(0)
        # dodajemy tyle krawędzi ile wynosi stopień
        for i in range(max_degree):
            # obniżamy stopnie nowym sąsiadom
            indexed_degrees[i][1]-=1
            graph.add_edge(max_node,indexed_degrees[i][0])
        
        indexed_degrees.sort(key=lambda x: x[1], reverse=True)
    return graph
           


def draw(graph: nx.Graph, name: str):
    pos = nx.circular_layout(graph)
    nx.draw(graph, pos, with_labels=True)
    plt.title(name)
    plt.savefig(name + ".png")
    plt.clf()

def main():
    seq=[4,2,2,3,2,1,4,2,2,2,2]
    print("Testing sequence: "+str(seq))
    graph=graph_from_sequence(seq)
    if graph:
        print("Generating graph from sequence: " +str(seq))
        draw(graph,"cw_1")

if __name__ == "__main__":
    main()