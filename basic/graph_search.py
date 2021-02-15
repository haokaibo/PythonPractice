'''
Given a sets of vertices and edges, search the graph by DFS(Depth First Search).
'''


class Graph:
    def __init__(self, vertexes, edges):
        self.vertexes = vertexes
        self.edges = edges


vertexes = ['A', 'B', 'C', 'D', 'E', 'F']
edges = {
    'A': ['B'],
    'B': ['A', 'C', 'D'],
    'C': ['B', 'D'],
    'D': ['B', 'C'],
    'E': ['F'],
    'F': ['E']
}
g = Graph(vertexes, edges)

visited = set()


def visit(v: str, g: Graph):
    print(v)
    visited.add(v)
    for e in g.edges[v]:
        if e not in visited:
            visit(e, g)


def DFS(g: Graph):
    if g is None or g.vertexes is None or len(g.vertexes) == 0:
        return

    for v in g.vertexes:
        if v not in visited:
            visit(v, g)


DFS(g)
