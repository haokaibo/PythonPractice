from unittest import TestCase

from basic.vertex_matrix import Graph, Vertex


class VertexMatrix(TestCase):
    def test_vertex_matrix(self):
        g = Graph()
        a = Vertex('A')
        g.add_vertx(a)
        g.add_vertx(Vertex('B'))
        for i in range(ord('A'), ord('K')):
            g.add_vertx(Vertex(chr(i)))

        edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'IH']
        for e in edges:
            g.add_edge(e[0], e[1])

        g.print_graph()