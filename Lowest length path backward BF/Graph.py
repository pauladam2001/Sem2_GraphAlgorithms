"""
Design and implement an abstract data type directed graph and a function (either a member function or an external one,
 as your choice) for reading a directed graph from a text file.

The vertices will be specified as integers from 0 to n-1, where n is the number of vertices.

Edges may be specified either by the two endpoints (that is, by the source and target), or by some abstract data type
Edge_id (that data type may be a pointer or reference to the edge representation, but without exposing
the  implementation details of the graph).

Additionally, create a map that associates to an edge an integer value (for instance, a cost).

Required operations:

->  g̶e̶t̶ ̶t̶h̶e̶ ̶n̶u̶m̶b̶e̶r̶ ̶o̶f̶ ̶v̶e̶r̶t̶i̶c̶e̶s̶;̶
-̶>̶ ̶p̶a̶r̶s̶e̶ ̶(̶i̶t̶e̶r̶a̶t̶e̶)̶ ̶t̶h̶e̶ ̶s̶e̶t̶ ̶o̶f̶ ̶v̶e̶r̶t̶i̶c̶e̶s̶;̶
-̶>̶ ̶g̶i̶v̶e̶n̶ ̶t̶w̶o̶ ̶v̶e̶r̶t̶i̶c̶e̶s̶,̶ ̶f̶i̶n̶d̶ ̶o̶u̶t̶ ̶w̶h̶e̶t̶h̶e̶r̶ ̶t̶h̶e̶r̶e̶ ̶i̶s̶ ̶a̶n̶ ̶e̶d̶g̶e̶ ̶f̶r̶o̶m̶ ̶t̶h̶e̶ ̶f̶i̶r̶s̶t̶ ̶o̶n̶e̶ ̶t̶o̶ ̶t̶h̶e̶ ̶s̶e̶c̶o̶n̶d̶ ̶o̶n̶e̶,̶ ̶a̶n̶d̶ ̶r̶e̶t̶r̶i̶e̶v̶e̶ ̶t̶h̶e̶ ̶E̶d̶g̶e̶_̶i̶d̶
̶i̶f̶ ̶t̶h̶e̶r̶e̶ ̶i̶s̶ ̶a̶n̶ ̶e̶d̶g̶e̶ ̶(̶t̶h̶e̶ ̶l̶a̶t̶t̶e̶r̶ ̶i̶s̶ ̶n̶o̶t̶ ̶r̶e̶q̶u̶i̶r̶e̶d̶ ̶i̶f̶ ̶a̶n̶ ̶e̶d̶g̶e̶ ̶i̶s̶ ̶r̶e̶p̶r̶e̶s̶e̶n̶t̶e̶d̶ ̶s̶i̶m̶p̶l̶y̶ ̶a̶s̶ ̶a̶ ̶p̶a̶i̶r̶ ̶o̶f̶ ̶v̶e̶r̶t̶e̶x̶ ̶i̶d̶e̶n̶t̶i̶f̶i̶e̶r̶s̶)̶;̶
-̶>̶ ̶g̶e̶t̶ ̶t̶h̶e̶ ̶i̶n̶ ̶d̶e̶g̶r̶e̶e̶ ̶a̶n̶d̶ ̶t̶h̶e̶ ̶o̶u̶t̶ ̶d̶e̶g̶r̶e̶e̶ ̶o̶f̶ ̶a̶ ̶s̶p̶e̶c̶i̶f̶i̶e̶d̶ ̶v̶e̶r̶t̶e̶x̶;̶
-> parse (iterate) the set of outbound edges of a specified vertex (that is, provide an iterator). For each outbound edge,
 the iterator shall provide the Edge_id of the current edge (or the target vertex, if no Edge_id is used).
-> parse the set of inbound edges of a specified vertex (as above);
-> get the endpoints of an edge specified by an Edge_id (if applicable);
-> retrieve or modify the information (the integer) attached to a specified edge.
-> The graph shall be modifiable: it shall be possible to add and remove an edge, and to add and remove a vertex. Think
about what should happen with the properties of existing edges and with the identification of remaining vertices.
You may use an abstract Vertex_id instead of an int in order to identify vertices; in this case, provide a way of
iterating the vertices of the graph.
-> The graph shall be copyable, that is, it should be possible to make an exact copy of a graph, so that the original
can be then modified independently of its copy. Think about the desirable behaviour of an Edge_property attached to the
original graph, when a copy is made.
-> Read the graph from a text file (as an external function); see the format below.
-> Write the graph to a text file (as an external function); see the format below.
-> Create a random graph with specified number of vertices and of edges (as an external function).
"""

import copy
from random import randint


def read_graph(graph, name_of_file):
    file = open(name_of_file, "rt")
    content = file.readlines()
    file.close()
    first_line = content[0]
    first_line = first_line.split(" ")

    number_of_vertices = int(first_line[0])
    number_of_edges = int(first_line[1][:-1])
    graph.number_of_edges = number_of_edges

    for vertex in range(0, number_of_vertices):
        new_vertex = Vertex(graph.current_vertex_id)
        graph.current_vertex_id += 1
        graph.outbound_edges[new_vertex.id] = []
        graph.inbound_edges[new_vertex.id] = []

    for line in range(1, graph.number_of_edges + 1):
        data = content[line].split(" ")
        source_vertex = Vertex(int(data[0]))
        target_vertex = Vertex(int(data[1]))
        cost = int(data[2][:-1])

        graph.add_edge(source_vertex.id, target_vertex.id, cost)


def write_graph(graph, name_of_file):
    file = open(name_of_file, 'wt')

    # the first line
    line = str(graph.number_of_vertices) + ' ' + str(graph.number_of_edges)
    file.write(line)
    file.write('\n')

    # the edges
    for vertex in graph.outbound_edges.keys():
        for edge in graph.outbound_edges[vertex]:
            line = str(edge)
            file.write(line)
            file.write('\n')

    file.close()


def create_random_graph(number_of_vertices, number_of_edges):
    if number_of_vertices <= 0:
        raise ValueError("The number of vertices must be positive.")
    if number_of_edges < 0:
        raise ValueError("The number of edges must be >= 0.")

    if number_of_edges > number_of_vertices**2:
        raise ValueError("The number of edges cannot be greater than the number of vertices squared.")

    graph = Graph()
    for vertex in range(0, number_of_vertices):
        new_vertex = Vertex(graph.current_vertex_id)
        graph.current_vertex_id += 1
        graph.outbound_edges[new_vertex.id] = []
        graph.inbound_edges[new_vertex.id] = []

    while graph.number_of_edges < number_of_edges:
        source = randint(0, number_of_vertices-1)
        target = randint(0, number_of_vertices-1)
        edge_cost = randint(-100, 100)

        if not graph.is_edge_from_to(source, target):
            graph.add_edge(source, target, edge_cost)

    return graph


class Edge:
    def __init__(self, edge_id, source_vertex_id, target_vertex_id, cost):
        self.__edge_id = edge_id
        self.__source = source_vertex_id
        self.__target = target_vertex_id
        self.__cost = cost

    @property
    def edge_id(self):
        return self.__edge_id

    @property
    def source_id(self):
        return self.__source

    @property
    def target_id(self):
        return self.__target

    @property
    def cost(self):
        return self.__cost

    @cost.setter
    def cost(self, value):
        self.__cost = value

    def __str__(self):
        return str(self.source_id) + " -> " + str(self.target_id) + "   cost " + str(self.cost)


class Vertex:
    def __init__(self, _id):
        self.__vertex_id = _id

    @property
    def id(self):
        return self.__vertex_id

    def __eq__(self, other):
        return self.id == other.id

    def __hash__(self):
        return hash(repr(self))


class Graph:
    def __init__(self):
        self.__number_of_edges = 0
        self.__outbound_edges = {}
        self.__inbound_edges = {}
        self.__current_edge_id = 1
        self.__current_vertex_id = 0

    @property
    def number_of_edges(self):
        return self.__number_of_edges

    @number_of_edges.setter
    def number_of_edges(self, value):
        self.__number_of_edges = value

    @property
    def outbound_edges(self):
        return self.__outbound_edges

    @property
    def inbound_edges(self):
        return self.__inbound_edges

    @property
    def current_edge_id(self):
        return self.__current_edge_id

    @current_edge_id.setter
    def current_edge_id(self, value):
        self.__current_edge_id = value

    @property
    def current_vertex_id(self):
        return self.__current_vertex_id

    @current_vertex_id.setter
    def current_vertex_id(self, value):
        self.__current_vertex_id = value

    @property
    def number_of_vertices(self):
        return len(self.outbound_edges)

    def parse_vertices(self):
        # for vertex in self.outbound_neighbours.keys():
        #     yield vertex
        return self.outbound_edges.keys()

    def parse_outbound_edges(self, vertex_id):
        if vertex_id not in self.outbound_edges.keys():
            raise ValueError("The given vertex does not exist.")
        for edge in self.outbound_edges[vertex_id]:
            yield edge

        # return self.outbound_edges[vertex_id]

    def parse_inbound_edges(self, vertex_id):
        if vertex_id not in self.inbound_edges.keys():
            raise ValueError("The given vertex does not exist.")

        for edge in self.inbound_edges[vertex_id]:
            yield edge

        # return self.inbound_edges[vertex_id]

    def is_edge_from_to(self, vertex_a_id, vertex_b_id):
        if vertex_a_id not in self.outbound_edges.keys() or vertex_b_id not in self.outbound_edges.keys():
            raise ValueError("The given vertex does not exist.")
        for edge in self.outbound_edges[vertex_a_id]:
            if edge.target_id == vertex_b_id:
                return edge.edge_id

        return 0

    def get_in_degree(self, vertex_id):
        if vertex_id not in self.outbound_edges.keys():
            raise ValueError("The given vertex does not exist.")

        # return len(self.inbound_edges[vertex_id])

        in_degree = 0
        for edge in self.inbound_edges[vertex_id]:
            in_degree += 1

        return in_degree

    def get_out_degree(self, vertex_id):
        if vertex_id not in self.outbound_edges.keys():
            raise ValueError("The given vertex does not exist.")

        # return len(self.outbound_edges[vertex_id])

        out_degree = 0
        for edge in self.outbound_edges[vertex_id]:
            out_degree += 1

        return out_degree

    def get_endpoints_of_an_edge(self, edge_id):
        source_and_target = []
        for vertex in self.outbound_edges.keys():
            for edge in self.outbound_edges[vertex]:
                if edge.edge_id == edge_id:
                    source_and_target.append(edge.source_id)
                    source_and_target.append(edge.target_id)
                    return source_and_target

        raise ValueError("There is no edge with the given id.")

    def get_cost_of_edge(self, edge_id):
        # if source_vertex_id not in self.outbound_edges.keys() or target_vertex_id not in self.outbound_edges.keys():
        #     raise ValueError("The given vertex does not exist.")
        #
        # for edge in self.outbound_edges[source_vertex_id]:
        #     if edge.target_id == target_vertex_id:
        #         return edge.cost

        for vertex in self.outbound_edges.keys():
            for edge in self.outbound_edges[vertex]:
                if edge.edge_id == edge_id:
                    return edge.cost
        raise ValueError("There is no edge between the given vertices.")


    def update_cost_of_edge(self, edge_id, new_value):

        # if source_vertex_id not in self.outbound_edges.keys() or target_vertex_id not in self.outbound_edges.keys():
        #     raise ValueError("The given vertex does not exist.")
        #
        # for edge in self.outbound_edges[source_vertex_id]:
        #     if edge.target_id == target_vertex_id:
        #         edge.cost = new_value
        #         return

        for vertex in self.outbound_edges.keys():
            for edge in self.outbound_edges[vertex]:
                if edge.edge_id == edge_id:
                    edge.cost = new_value
                    return

        raise ValueError("There is no edge with the given id.")

    def add_edge(self, source_vertex_id, target_vertex_id, edge_cost):
        if source_vertex_id not in self.inbound_edges.keys():
            raise ValueError("The source vertex does not exist.")

        if target_vertex_id not in self.inbound_edges.keys():
            raise ValueError("The target vertex does not exist.")

        if self.is_edge_from_to(source_vertex_id, target_vertex_id):
            raise ValueError("There already exists an edge between these vertices.")

        new_edge = Edge(self.current_edge_id, source_vertex_id, target_vertex_id, edge_cost)

        self.outbound_edges[source_vertex_id].append(new_edge)
        self.inbound_edges[target_vertex_id].append(new_edge)

        self.current_edge_id += 1
        self.number_of_edges += 1

    def remove_edge(self, edge_id):
        # if source_vertex_id not in self.outbound_edges.keys() or target_vertex_id not in self.outbound_edges.keys():
        #     raise ValueError("The given vertex does not exist.")
        #
        # for edge in self.outbound_edges[source_vertex_id]:
        #     if edge.target_id == target_vertex_id:
        #         self.outbound_edges[source_vertex_id].remove(edge)
        #         return

        for vertex in self.outbound_edges.keys():
            for edge in self.outbound_edges[vertex]:
                if edge.edge_id == edge_id:
                    self.outbound_edges[vertex].remove(edge)
                    return
        raise ValueError("There is no edge with the given id.")

    def add_vertex(self):
        new_vertex = Vertex(self.current_vertex_id)
        self.current_vertex_id += 1
        self.outbound_edges[new_vertex.id] = []

    def remove_vertex(self, vertex_id):
        if vertex_id not in self.outbound_edges.keys():
            raise ValueError("The vertex with the given id does not exist.")

        # remove its outbound edges
        del self.outbound_edges[vertex_id]
        del self.inbound_edges[vertex_id]

        # delete its inbound edges coming out from other vertices
        for vertex in self.outbound_edges.keys():
            for edge in self.outbound_edges[vertex]:
                if edge.target_id == vertex_id:
                    self.outbound_edges[vertex].remove(edge)
            for edge in self.inbound_edges[vertex]:
                if edge.source_id == vertex_id:
                    self.inbound_edges[vertex].remove(edge)

    def copy(self):
        copy_of_graph = copy.deepcopy(self)
        return copy_of_graph