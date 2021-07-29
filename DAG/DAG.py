from graph import Graph
import copy

class DAGLab4(Graph):
    def __init__(self):
        super(DAGLab4, self).__init__()
        self._durations = {}
        self._prerequisites = {}

    def init_durations(self):
        for vertex in range(0, 6):
            self._durations[vertex] = []

        self._durations[0].append(1)
        self._durations[1].append(4)
        self._durations[2].append(1)
        self._durations[3].append(3)
        self._durations[4].append(2)
        self._durations[5].append(5)

    def init_prerequisites(self):
        for vertex in range(0, 10):
            self._prerequisites[vertex] = []

        self._prerequisites[0] = float('inf')   # no prerequisites
        self._prerequisites[1].append(0)
        self._prerequisites[3] = float('inf')   # no prerequisites
        self._prerequisites[4] = float('inf')   # no prerequisites
        self._prerequisites[1].append(3)
        self._prerequisites[1].append(4)
        self._prerequisites[2].append(1)
        self._prerequisites[2].append(5)
        self._prerequisites[5].append(4)

    def create_corresponding_graph(self):
        self.nr_of_vertices = len(self._durations)
        self._nr_of_edges = 0
        self.initialize_graph()
        for vertex in range(self.nr_of_vertices):
            if self._prerequisites[vertex] != float('inf'):
                for prereq in self._prerequisites[vertex]:
                    self.add_edge(prereq, vertex, 0)

    def TopSortPredecessorCounting(self):
        sorted = []
        q = []  # queue
        count = {}
        for vertex in self.parse_vertices():
            count[vertex] = self.get_in_degree(vertex)
            if count[vertex] == 0:
                q.append(vertex)
        while len(q) != 0:
            vertex = q.pop(0)
            sorted.append(vertex)
            for y in self.parse_out_edges(vertex):
                count[y] = count[y] - 1
                if count[y] == 0:
                    q.append(y)
        if len(sorted) < self.nr_of_vertices:
            sorted = None
        return sorted

    # For the earliest scheduling we compute the scheduling of all the prerequisites and the start time is the max between the ending times
    # of the prerequisites.
    # start(x) = max(end(y)) : x depends on y (0 if no prerequisites)
    # end(x) = start(x) + duration(x)

    def earliest_scheduling(self, sorted):
        auxDurations = copy.deepcopy(self._durations)
        for vertex in sorted:
            if self._prerequisites[vertex] == float('inf'):
                auxDurations[vertex] = []
                duration = self._durations[vertex][0]
                auxDurations[vertex].append(0)                                        # start
                auxDurations[vertex].append(auxDurations[vertex][0] + duration)       # end
            else:
                maxEnd = 0
                for prereq in self._prerequisites[vertex]:
                    if auxDurations[prereq][1] > maxEnd:
                        maxEnd = auxDurations[prereq][1]
                auxDurations[vertex] = []
                duration = self._durations[vertex][0]
                auxDurations[vertex].append(maxEnd)                                 # start
                auxDurations[vertex].append(auxDurations[vertex][0] + duration)     # end
        return auxDurations

    # For the latest scheduling we start from right (end of project) and move towards left.
    # end(x) = min(start(y)) : y depends on x (project duration if nothing depends on x)
    # start(x) = end(x) - duration(x)

    def latest_scheduling(self, sorted, projectDuration):
        auxDurations = copy.deepcopy(self._durations)
        for vertex in reversed(sorted):
            sem = 1
            for key in self._prerequisites.keys():
                if self._prerequisites[key] != float('inf'):
                    for val in self._prerequisites[key]:
                        if vertex == val:
                            sem = 0
            if sem == 1:
                auxDurations[vertex] = []
                duration = self._durations[vertex][0]
                auxDurations[vertex].append(projectDuration - duration)             # start
                auxDurations[vertex].append(projectDuration)                        # end
            else:
                maxStart = projectDuration + 1
                for key in reversed(sorted):
                    if self._prerequisites[key] != float('inf'):
                        for val in self._prerequisites[key]:
                            if vertex == val:
                                if auxDurations[key][0] < maxStart:
                                    maxStart = auxDurations[key][0]
                auxDurations[vertex] = []
                duration = self._durations[vertex][0]
                auxDurations[vertex].append(maxStart - duration)                    # start
                auxDurations[vertex].append(maxStart)                               # end
        return auxDurations
