from unittest import TestCase

from basic.vertex_list import Graph
from basic.vertex_list import Vertex

# codetiming is an optional dev dependency; fall back to a no-op so the test
# suite collects and runs even when it's not installed.
try:
    from codetiming import Timer
except ImportError:  # pragma: no cover - import guard
    def Timer(_name):
        def decorator(func):
            return func
        return decorator


class GraphTest(TestCase):
    @Timer('test_graph')
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