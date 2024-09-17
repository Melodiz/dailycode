import networkx as nx
import itertools
import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

def generate(number_of_edges, number_of_pendant_vertices):
    all_graphs = []
    for num_edges in range(1,number_of_edges):
        for num_nodes in range(number_of_edges+1):
            graphs = [G for G in nx.graph_atlas_g() if G.number_of_nodes() == num_nodes and G.number_of_edges() == number_of_edges and nx.is_connected(G)]
            all_graphs.extend(graphs)
    return all_graphs    

def filter_by_pendant_vertices(G, number_of_pendant_vertices):
    return sum(1 for _, degree in G.degree() if degree == 1) == number_of_pendant_vertices


def draw_graphs(graphs):
    for i, graph in enumerate(graphs):
        plt.figure(i)
        nx.draw_circular(graph, with_labels=True)
    plt.show()


def filter_isomorphic(graphs):
    non_isomorphic_graphs = []
    for i in range(len(graphs)):
        flag = False
        for j in range(i+1, len(graphs)):
            if nx.is_isomorphic(graphs[i], graphs[j]):
                flag = True
                break
        if not flag:  
            non_isomorphic_graphs.append(graphs[i])
    return non_isomorphic_graphs


non_isomorphic_graphs = generate(7, 2)
print(len(non_isomorphic_graphs))

with_two_pendant = [G for G in non_isomorphic_graphs if filter_by_pendant_vertices(G, 2)]
print(len(with_two_pendant))
draw_graphs(with_two_pendant)