import random, copy


class GraphException(Exception):
    def __init__(self, message):
        self._message = message
    def __str__(self):
        return self._message


class Graph:
    def __init__(self):
        self._dictionaryIN = {}
        self._dictionaryOUT = {}
        self._dictionaryCost = {}
        self._nr_of_vertices = 0
        self._nr_of_edges = 0

    @property
    def nr_of_vertices(self):
        return self._nr_of_vertices

    @property
    def nr_of_edges(self):
        return self._nr_of_edges

    @property
    def dictionaryOUT(self):
        return self._dictionaryOUT

    @nr_of_vertices.setter
    def nr_of_vertices(self, value):
        self._nr_of_vertices = value

    @nr_of_edges.setter
    def nr_of_edges(self, value):
        self._nr_of_edges = value

    def new_vertex(self, vertex):
        self._dictionaryIN[vertex] = []
        self._dictionaryOUT[vertex] = []

    def add_vertex(self):
        self.new_vertex(self._nr_of_vertices)
        self._nr_of_vertices += 1

    def remove_vertex(self, vertex):
        if self.is_vertex(vertex) == False:
            raise GraphException('Vertex does not exist!')

        copy_of_dictIN = self._dictionaryIN[vertex][:]    # [:] - slicing; copy of array from start to end
        for vertice in copy_of_dictIN:
            self.remove_edge(vertice, vertex)
        del self._dictionaryIN[vertex]

        copy_of_dictOUT = self._dictionaryOUT[vertex][:]
        for vertice in copy_of_dictOUT:
            self.remove_edge(vertex, vertice)
        del self._dictionaryOUT[vertex]

        self._nr_of_vertices -= 1

        # we remove the cost in the remove_edge function

    def initialize_graph(self):
        self._dictionaryIN.clear()
        self._dictionaryOUT.clear()
        self._dictionaryCost.clear()
        for vertex in range(self._nr_of_vertices):
            self.new_vertex(vertex)

    def is_edge(self, vertex1, vertex2): #vertex1 = source vertex, vertex2 = destination vertex
        if self.is_vertex(vertex1) == False:
            return False
        for vertex in self._dictionaryOUT[vertex1]:
            if vertex == vertex2:
                return True
        return False

    def is_vertex(self, vertex):
        if vertex in self._dictionaryIN.keys() or vertex in self._dictionaryOUT.keys():
            return True
        return False

    def parse_vertices(self):
        # The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable
        # function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run.
        # This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list

        for vertex in self._dictionaryIN.keys():
            yield vertex

    def get_in_degree(self, vertex):
        if self.is_vertex(vertex) == False:
            raise GraphException('Invalid vertex!')

        return len(self._dictionaryIN[vertex])

    def get_out_degree(self, vertex):
        if self.is_vertex(vertex) == False:
            raise GraphException('Invalid vertex!')

        return len(self._dictionaryOUT[vertex])

    def add_edge(self, vertex1, vertex2, cost):
        if self.is_vertex(vertex1) == False or self.is_vertex(vertex2) == False:
            raise GraphException('Invalid vertices!')
        if self.is_edge(vertex1, vertex2):
            raise GraphException('Edge already exists!')

        self._dictionaryIN[vertex2].append(vertex1)
        self._dictionaryOUT[vertex1].append(vertex2)
        self._nr_of_edges += 1
        self._dictionaryCost[(vertex1, vertex2)] = cost

    def remove_edge(self, vertex1, vertex2):
        if self.is_vertex(vertex1) == False or self.is_vertex(vertex2) == False:
            raise GraphException('Invalid vertices!')
        if self.is_edge(vertex1, vertex2) == False:
            raise GraphException('Edge does not exist!')

        self._dictionaryIN[vertex2].remove(vertex1)
        self._dictionaryOUT[vertex1].remove(vertex2)
        del self._dictionaryCost[(vertex1, vertex2)]
        self._nr_of_edges -= 1

    def get_edge_cost(self, vertex1, vertex2):
        if self.is_edge(vertex1, vertex2) == False:
            raise GraphException('Edge does not exist!')

        return self._dictionaryCost[(vertex1, vertex2)]

    def modify_edge_cost(self, vertex1, vertex2, newCost):
        if self.is_edge(vertex1, vertex2) == False:
            raise GraphException('Edge does not exist!')

        self._dictionaryCost[(vertex1, vertex2)] = newCost

    def parse_in_edges(self, vertex):
        if self.is_vertex(vertex) == False:
            raise GraphException('Invalid vertex!')

        for edge in self._dictionaryIN[vertex]:
            yield edge

    def parse_out_edges(self, vertex):
        if self.is_vertex(vertex) == False:
            raise GraphException('Invalid vertex!')

        for edge in self._dictionaryOUT[vertex]:
            yield edge

    def copy_of_graph(self):
        return copy.deepcopy(self)




def create_random_graph(graph, nr_of_vertices, nr_of_edges):
    if nr_of_vertices * nr_of_vertices < nr_of_edges:
        raise GraphException('Invalid number of edges or vertices!')

    graph._nr_of_vertices = nr_of_vertices
    graph._nr_of_edges = 0
    graph.initialize_graph()
    while nr_of_edges > 0:
        vertex1 = random.randint(0, graph._nr_of_vertices - 1)
        vertex2 = random.randint(0, graph._nr_of_vertices - 1)
        try:
            cost = random.randint(-50, 50)
            graph.add_edge(vertex1, vertex2, cost)
            nr_of_edges -= 1
        except:
            continue

def read_graph(graph):
    try:
        file = open('input.txt', 'rt')
       #file = open('1k4k.txt', 'rt')
        # file = open('10k40k.txt', 'rt')
        # file = open('100k400k.txt', 'rt')
        #file = open('C:\\Users\\paula\\OneDrive\\Desktop\\graph1m.txt', 'rt')
       # content = file.readlines()
       # file.close()

        sem = 0
        for line in file:
            if sem == 0: #first line
                line = line.split(' ')
                graph._nr_of_vertices = int(line[0])
                graph._nr_of_edges = 0

                graph.initialize_graph()

                sem = 1
            else:
                line = line.split(' ')
                source_vertex = int(line[0])
                destination_vertex = int(line[1])
                cost = int(line[2])
                graph.add_edge(source_vertex, destination_vertex, cost)
    except IOError as ioe:
        raise GraphException('An error occured!' + str(ioe))

def write_graph(graph):
    try:
        file = open('output.txt', 'wt')

        #first line
        line = str(graph._nr_of_vertices) + ' ' + str(graph._nr_of_edges)
        file.write(line)
        file.write('\n')
        for vertex in graph._dictionaryOUT.keys():
            for vertex2 in graph._dictionaryOUT[vertex]:
                line = str(vertex) + ' ' + str(vertex2) + ' ' + str(graph._dictionaryCost[(vertex, vertex2)])
                file.write(line)
                file.write('\n')
        file.close()
    except Exception as e:
        raise GraphException('An error occured!' + str(e))
