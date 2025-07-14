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
    print('DFS now..')
    if g is None or g.vertexes is None or len(g.vertexes) == 0:
        return

    for v in g.vertexes:
        if v not in visited:
            visit(v, g)


DFS(g)

to_be_visit = set()


def visit2(v, g):
    print(v)
    for e in g.edges[v]:
        to_be_visit.add(e)


def BFS(g: Graph):
    print('BFS now...')
    if g is None or g.vertexes is None or len(g.vertexes) == 0:
        return

    for v in g.vertexes:
        visit(v, g)

    while len(to_be_visit) > 0:
        for v in to_be_visit:
            visit2(v)

BFS(g)
