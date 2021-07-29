from Graph import Graph, read_graph, write_graph, create_random_graph

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
-> Write the graph from a text file (as an external function); see the format below.
-> Create a random graph with specified number of vertices and of edges (as an external function).
"""


class UI:
    def __init__(self, graph):
        self._graph = graph


    @property
    def graph(self):
        return self._graph

    def print_menu(self):
        print("1. Read a graph from a file.\n")
        print("2. Write the graph to a file.\n")
        print("3. Get the number of vertices.\n")
        print("4. Parse the set of vertices.\n")
        print("5. Is edge between 2 vertices?\n")
        print("6. Get the in degree of a vertex.\n")
        print("7. Get the out degree of a vertex.\n")
        print("8. Parse the outbound edges of a vertex.\n")
        print("9. Parse the inbound edges of a vertex.\n")
        print("10. Get the endpoints of an edge.\n")
        print("11. Get the cost of an edge.\n")
        print("12. Update the cost of an edge.\n")
        print("13. Add an edge.\n")
        print("14. Remove an edge.\n")
        print("15. Add a vertex.\n")
        print("16. Remove a vertex.\n")
        print("17. Copy the graph.\n")
        print("18. Create a random graph.\n")
        print("19. Print the graph.\n")
        print("20. Exit.\n")

    def read_graph_ui(self, name_of_file):
        read_graph(self.graph, name_of_file)
        print("Graph read successfully.\n")

    def write_graph_ui(self, name_of_file):
        write_graph(self.graph, name_of_file)
        print("Graph written to file successfully.\n")

    def get_number_of_vertices_ui(self):
        number_of_vertices = self.graph.number_of_vertices()
        print("The graph has " + str(number_of_vertices) + " vertices.\n")

    def parse_the_set_of_vertices_ui(self):
        for vertex in self.graph.parse_vertices():
            print(vertex)

    def is_edge_between_vertices_ui(self):
        vertex_a = int(input("Source vertex: "))
        vertex_b = int(input("Target vertex: "))
        edge = self.graph.is_edge_from_to(vertex_a, vertex_b)
        if edge:
            print("Yes. Edge " + str(edge) + "\n")
        else:
            print("There is no edge from " + str(vertex_a) + " to " + str(vertex_b) + ".\n")

    def get_in_degree_ui(self):
        vertex_id = int(input("Enter vertex: "))
        vertex_in_degree = self.graph.get_in_degree(vertex_id)
        print("The in-degree of vertex " + str(vertex_id) + " is " + str(vertex_in_degree) + ".\n")

    def get_out_degree_ui(self):
        vertex_id = int(input("Enter vertex: "))
        vertex_out_degree = self.graph.get_out_degree(vertex_id)
        print("The out-degree of vertex " + str(vertex_id) + " is " + str(vertex_out_degree) + ".\n")

    def parse_outbound_edges_of_vertex_ui(self):
        vertex_id = int(input("Enter vertex: "))
        outbound_edges = self.graph.parse_outbound_edges(vertex_id)
        if outbound_edges:
            print("The outbound edges are: \n")
            for edge in outbound_edges:
                print(edge)
        else:
            print("The vertex does not have outbound edges.\n")

    def parse_inbound_edges_of_vertex_ui(self):
        vertex_id = int(input("Enter vertex: "))
        inbound_edges = self.graph.parse_inbound_edges(vertex_id)
        if inbound_edges:
            print("The inbound edges are: \n")
            for edge in inbound_edges:
                print(edge)
        else:
            print("The vertex does not have inbound edges.\n")

    def get_endpoints_of_edge_ui(self):
        edge_id = int(input("Edge id: "))
        source, target = self.graph.get_endpoints_of_an_edge(edge_id)
        print("The edge " + str(edge_id) + " goes from " + str(source) + " to " + str(target) + ".")

    def get_cost_of_edge_ui(self):
        edge_id = int(input("Edge id: "))
        edge_cost = self.graph.get_cost_of_edge(edge_id)
        print("The cost of the edge is " + str(edge_cost) + ".")

    def update_cost_of_edge_ui(self):
        edge_id = int(input("Edge id: "))
        new_cost = int(input("New cost: "))
        self.graph.update_cost_of_edge(edge_id, new_cost)
        print("Cost was updated successfully.\n")

    def add_edge_ui(self):
        source_vertex = int(input("Source vertex: "))
        target_vertex = int(input("Target vertex: "))
        edge_cost = int(input("Edge cost: "))
        self.graph.add_edge(source_vertex, target_vertex, edge_cost)
        print("Edge was added successfully.\n")

    def remove_edge_ui(self):
        edge_id = int(input("Edge id: "))
        self.graph.remove_edge(edge_id)
        print("Edge was removed successfully.\n")

    def add_vertex_ui(self):
        self.graph.add_vertex()
        print("Vertex was added successfully.\n")

    def remove_vertex_ui(self):
        vertex_id = int(input("Vertex id: "))
        self.graph.remove_vertex(vertex_id)
        print("Vertex was removed successfully.\n")

    def deepcopy_ui(self):
        print("The graph was copied.\n")

        if self.graph.is_edge_from_to(2, 1) > 0:
            print("True")  # should be true
        else:
            print("False")

        copy_of_graph = self.graph.copy()

        if copy_of_graph.is_edge_from_to(2, 1) > 0:
            print("True")  # should be true
        else:
            print("False")
        copy_of_graph.remove_vertex(2)

        try:
            copy_of_graph.is_edge_from_to(2, 1)
            assert False
        except ValueError:
            assert True

        if self.graph.is_edge_from_to(2, 1) > 0:
            print("True")  # should be true
        else:
            print("False")

    def create_random_graph_ui(self):
        number_of_vertices = int(input("Number of vertices: "))
        number_of_edges = int(input("Number of edges: "))
        print(create_random_graph(number_of_vertices, number_of_edges))

    def print_graph(self):
        print(self.graph)

    def start(self):
        self.print_menu()
        not_finished = 1
        input_file = "input_data.txt"
        output_file = "output_data.txt"
        options = {3: self.get_number_of_vertices_ui,
                   4: self.parse_the_set_of_vertices_ui, 5: self.is_edge_between_vertices_ui, 6: self.get_in_degree_ui,
                   7: self.get_out_degree_ui, 8: self.parse_outbound_edges_of_vertex_ui,
                   9: self.parse_inbound_edges_of_vertex_ui, 10: self.get_endpoints_of_edge_ui,
                   11: self.get_cost_of_edge_ui, 12: self.update_cost_of_edge_ui, 13: self.add_edge_ui,
                   14: self.remove_edge_ui, 15: self.add_vertex_ui, 16: self.remove_vertex_ui,
                   17: self.deepcopy_ui, 18: self.create_random_graph_ui, 19: self.print_graph}
        while not_finished:
            user_option = int(input("Enter option: "))
            if user_option == 1:
                try:
                    self.read_graph_ui(input_file)
                except Exception as exception_message:
                    print(exception_message)
            elif user_option == 2:
                try:
                    self.write_graph_ui(output_file)
                except Exception as exception_message:
                    print(exception_message)
            elif user_option in options:
                try:
                    options[user_option]()
                except Exception as exception_message:
                    print(exception_message)
            elif user_option == 20:
                not_finished = 0
            else:
                print("Invalid command.")


my_graph = Graph()
ui = UI(my_graph)
ui.start()
