from graph import Graph


class LowestCostDijkstraLab3(Graph):
    def __init__(self):
        super(LowestCostDijkstraLab3, self).__init__()
        self._values = {}

    def isEmpty(self):
        return len(self._values) == 0

    def pop(self):
        topPriority = None
        topObject = None
        for obj in self._values:
            objPriority = self._values[obj]
            if topPriority is None or topPriority > objPriority:
                topPriority = objPriority
                topObject = obj
        del self._values[topObject]
        return topObject

    def add(self, obj, priority):
        self._values[obj] = priority

    def Dijkstra(self, source_vertex, target_vertex):
        found = False
        prev = {}
        self.add(source_vertex, 0)      # second argument is priority
        dist = {}
        dist[source_vertex] = 0
        while not self.isEmpty() and not found:
            x = self.pop()          # dequeue the element with minimum priority
            for y in self.parse_out_edges(x):
                if y not in dist.keys() or dist[y] > dist[x] + self.get_edge_cost(x, y):
                    dist[y] = dist[x] + self.get_edge_cost(x, y)
                    self.add(y, dist[y])   # enqueue
                    prev[y] = x
            if x == target_vertex:
                found = True
        return dist, prev

    def getPath(self, source_vertex, target_vertex, prev):
        list = []
        while target_vertex != source_vertex:
            list.append(target_vertex)
            target_vertex = prev[target_vertex]
        path= [source_vertex]
        for i in range(len(list)):
            path.append(list[len(list) - i - 1])
        return path
