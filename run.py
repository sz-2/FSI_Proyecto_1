# Search methods

import search
import utils

ab = search.GPSProblem('A', 'B', search.romania)

zg = search.GPSProblem('Z', 'G', search.romania)

bl = search.GPSProblem('B', 'L', search.romania)


# Busqueda en profundidad
# print(search.depth_first_graph_search(ab).path())
# Result: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418


# Busqueda en amplitud
# print(search.breadth_first_graph_search(ab).path())
# RESULT: [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450


# Busquedad Metodo Branch and Bound
# print(search.method_branch_and_bound(bl).path())
# RESULT: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]


# Busquedad Metodo Branch and Bound con HEURISTICA
# print(search.method_branch_and_bound_Heuristic(bl).path())
# RESULT: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
