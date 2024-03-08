# G = (V,E)
# vertex edges
# V = {0,1,2,3}
# E = { (0,1), (0,2), (1,3), (2,3) }

from collections import namedtuple

Graph = namedtuple("Graph", ["nodes", "edges"])

def createGraphFromNodexEdges():
    nodes = ["A", "B", "C", "D"]
    edges = [
        ("A", "B"),
        ("A", "B"),
        ("A", "C"),
        ("A", "C"),
        ("A", "D"),
        ("B", "D"),
        ("C", "D"),
    ]

    return Graph(nodes, edges)

def adjacency_dict(graph):
    adj = {node: [] for node in graph.nodes}
    for edge in graph.edges:
        node1, node2 = edge[0], edge[1]
        adj[node1].append(node2)
        adj[node2].append(node1)

    return adj

def adjacency_matrix(graph):
    adj = [[0 for node in graph.nodes] for node in graph.nodes]
    for edge in graph.edges:
        node1,node2 = edge[0],edge[1]
        adj[node1][node2] += 1
        adj[node2][node1] += 1

    return adj

G1 = createGraphFromNodexEdges()
print(G1)

G2 = adjacency_dict(G1)
print(G2)

nodes = range(4)
edges = [
    (0,1),
    (0,1),
    (0,2),
    (0,2),
    (0,3),
    (1,3),
    (2,3),
]
G3 = Graph(nodes, edges)
print(adjacency_matrix(G3))

graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}