import numpy as np


class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)
        # If the graph is undirected, add the reverse edge as well
        if v not in self.graph:
            self.graph[v] = []
        self.graph[v].append(u)

    def display(self):
        for node in self.graph:
            print(f"{node} -> {' '.join(map(str, self.graph[node]))}")
            # print(self.graph[node])
        print(self.graph.keys())


# Create a graph instance
g = Graph()

# Add edges to the graph
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(1, 3)
g.add_edge(2, 3)
g.add_edge(3, 4)

# Display the adjacency list
g.display()
