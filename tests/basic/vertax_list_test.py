from unittest import TestCase

from basic.vertex_list import Graph
from basic.vertex_list import Vertex


class GraphTest(TestCase):
    def test_graph(self):
        g = Graph()
        a = Vertex('A')
        g.add_vertex(a)
        g.add_vertex(Vertex('B'))
        for i in range(ord('A'), ord('K')):
            g.add_vertex(Vertex(chr(i)))

        edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'IH']
        for e in edges:
            g.add_edge(e[0], e[1])

        g.print_graph()
