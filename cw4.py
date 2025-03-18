import matplotlib.pyplot as plt
import networkx as nx
import random

def generate_random_euler_graph(n):
    if n<=2:
        print("Graph of less than 3 nodes can't have Euler cycle")
        return None
    for i in range(50):
        degrees=generate_random_even_numbers(n)
        print(degrees)
        graph=graph_from_sequence(degrees)
        if graph is not None:
            draw(graph,"a")
            if len(find_connected_components(graph))==1:
                print("Euler cycle: "+str(find_euler_cycle(graph)))
                break
            else:
                print("graph is not connected")
        print("")
        
def generate_random_even_numbers(n):
    if n <= 2:
        return []

    even_numbers = []
    while len(even_numbers) < n:
        num = random.randint(1, n-1)
        if num % 2 == 0:
            even_numbers.append(num)
    
    return even_numbers

def find_euler_cycle(graph):
    if graph.number_of_edges()==0:
        return None
    return next_node(graph,list(graph.nodes())[0])

def next_node(graph,cur_node):
    if graph.number_of_edges()==0:
        return [cur_node]
    for node in graph.neighbors(cur_node):
        if graph.degree(node)==1 & graph.degree(cur_node)>1:
            continue
        graph_copy=graph.copy()
        graph_copy.remove_edge(cur_node,node)
        result=next_node(graph_copy,node)
        if result is not None:
            return [cur_node]+result
    return None

def find_connected_components(graph): #from cw3
    def dfs(v, component_id, component):
        comp[v] = component_id
        component.append(v)
        for neighbor in graph.neighbors(v):
            if comp[neighbor] == -1:
                dfs(neighbor, component_id, component)

    comp = {v: -1 for v in graph.nodes}
    components = []
    component_id = 0

    for v in graph.nodes:
        if comp[v] == -1:
            component_id += 1
            component = []
            dfs(v, component_id, component)
            components.append(component)

    components.sort(key=len, reverse=True)
    return components

def is_graphical_sequence(sequence): #from cw1
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

def graph_from_sequence(seq): #from cw1
    degrees=seq.copy()
    if not is_graphical_sequence(degrees):
        print("Given sequence is not a graphical sequence.")
        return None
    
    graph = nx.Graph()
    n = len(degrees)
    nodes = list(range(n))
    graph.add_nodes_from(nodes)
    
    degrees.sort(reverse=True)
    indexed_degrees = [[i, degrees[i]] for i in range(n)]
    while indexed_degrees[0][1]>0:
        max_node, max_degree =indexed_degrees.pop(0)
        for i in range(max_degree):
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
    generate_random_euler_graph(5)

if __name__ == "__main__":
    main()