"""
Test for shortest path utility functions.
"""

import unittest
from zen import *
import random


class Pred2PathTestCase(unittest.TestCase):

    def test_pred2path__dijkstra_(self):
        G = DiGraph()
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_node(4)

        D, P = dijkstra_path_(G, 0)

        self.assertEqual(pred2path_(0, 2, P), [0, 1, 2])

        self.assertEqual(pred2path_(0, 3, P), None)

    def test_pred2path_dijkstra(self):
        G = DiGraph()
        G.add_edge(1, 2)
        G.add_edge(2, 3)
        G.add_node(4)

        R = dijkstra_path(G, 1)

        self.assertEqual(pred2path(1, 3, R), [1, 2, 3])

        self.assertEqual(pred2path(1, 4, R), None)
