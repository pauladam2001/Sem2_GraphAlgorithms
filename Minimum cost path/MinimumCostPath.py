from graph import Graph


class MinimumCostPath(Graph):
    def __init__(self):
        super(MinimumCostPath, self).__init__()
        self._visited = []

    def init_visited(self):
        for i in range(0, self.nr_of_vertices):
            self._visited.append(i)
            self._visited[i] = 0

    def has_negative_cycles(self, source):
        infinity = float('inf')
        v = self.nr_of_vertices
        dist = [infinity for i in range(v)]
        dist[source] = 0

        for i in range(0, v):
            for vertex in self.parse_vertices():
                for edge in self.parse_out_edges(vertex):
                    edgeCost = self.get_edge_cost(vertex, edge)
                    if dist[vertex] != infinity and dist[vertex] + edgeCost < dist[edge]:
                        dist[edge] = dist[vertex] + edgeCost

        for vertex in self.parse_vertices():
            for edge in self.parse_out_edges(vertex):
                edgeCost = self.get_edge_cost(vertex, edge)
                if dist[vertex] != infinity and dist[vertex] + edgeCost < dist[edge]:
                    return True
        return False

    def minimum_cost_path(self, source, target):

        if source == target:        # stop condition, when we find the destination
            return 0

        self._visited[source] = 1  # mark the current source as visited

        minCost = float('inf')  # for now the minimum cost is infinity (doesn't exist)

        for vertex in self.parse_out_edges(source):  # parse the outbound edges of the current source
            if not self._visited[vertex]:            # if the vertex is not visited we compute the distance
                curr = self.minimum_cost_path(vertex, target)   # recursive function
                minCost = min(minCost, self.get_edge_cost(source, vertex) + curr)  # compute the minCost path

        self._visited[source] = 0   # unmark the source in order to make it available for the other paths

        return minCost  # return the minimum cost path


# 5 6
# 0 1 -1
# 0 3 1
# 1 2 -2            //another example
# 2 0 -3
# 3 2 -1
# 4 3 2