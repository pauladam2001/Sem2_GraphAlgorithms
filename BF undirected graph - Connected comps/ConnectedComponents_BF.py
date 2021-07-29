from graph import Graph


class ConnectedComponentsBFLab2(Graph):
    def __init__(self):
        super(ConnectedComponentsBFLab2, self).__init__()
        self._visited = [0] * self.nr_of_vertices

    @property
    def visited(self):
        return self._visited

    @visited.setter
    def visited(self, nrOfVertices):
        self._visited = [0] * nrOfVertices

    # def unvisited_vertex(self):
    #     for vertex in range(0, self.nr_of_vertices - 1):
    #         if self._visited[vertex] == 0:
    #             return vertex
    #     return -1

    def breadth_first_search(self, vertex, temporaryList):
        self._visited[vertex] = 1
        temporaryList.append(vertex)
        for index in self.dictionaryOUT[vertex]:
            if self._visited[index] == 0:
                temporaryList = self.breadth_first_search(index, temporaryList)
        return temporaryList

    def connected_components(self):
        connectedComponents = []
        for vertex in range(0, self.nr_of_vertices - 1):
            if self._visited[vertex] == 0:
                temporaryList = []
                connectedComponents.append(self.breadth_first_search(vertex, temporaryList))
        return connectedComponents
