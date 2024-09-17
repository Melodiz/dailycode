import networkx as nx
from networkx.generators.nonisomorphic_trees import nonisomorphic_trees
import matplotlib.pyplot as plt

def count_3degree_vertices(tree):
    return sum(1 for node in tree if tree.degree(node) == 1)

def main():
    num_vertices = 6 
    trees = nonisomorphic_trees(num_vertices)
    selected_trees = []
    
    count = 0
    for tree in trees:
        if count_3degree_vertices(tree) == 4:
            count += 1
        selected_trees.append(tree)
    
    print(f"Number of non-isomorphic trees with 7 edges and exactly 3 pendant vertices: {count}")
    draw_graphs(selected_trees)
    return selected_trees

def draw_graphs(graphs):
    for i, graph in enumerate(graphs):
        plt.figure(i)
        nx.draw(graph, with_labels=True)
    plt.show()

if __name__ == "__main__":
    main()