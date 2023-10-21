# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)



# Busqueda en profundidad
# print(search.depth_first_graph_search(ab).path())
# Result: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418

# Busqueda en amplitud
# print(search.breadth_first_graph_search(ab).path())
# RESULT: [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450


# Busquedad Metodo Branch and Bound
# print(search.method_branch_and_bound(ab).path())
