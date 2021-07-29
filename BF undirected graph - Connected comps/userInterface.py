from graph import Graph, GraphException, read_graph, write_graph, create_random_graph
from ConnectedComponents_BF import ConnectedComponentsBFLab2
import sys


class UI:
    def __init__(self):
        #self._graph = Graph()                      # directed graph - Lab 1
        self._graph = ConnectedComponentsBFLab2()   # undirected graph - Lab 2

    @staticmethod
    def exit_ui():
        print('See you later!')
        sys.exit(0)

    # def get_nr_of_vertices_ui(self):
    #     print('The number of vertices is ' + str(self._graph.nr_of_vertices))
    #
    # def parse_vertices_ui(self):
    #     print('The vertices are:')
    #     vertices = self._graph.parse_vertices()
    #     for vertex in vertices:
    #         print(vertex)
    #
    # def is_edge_ui(self):
    #     source_vertex = input('Source vertex: ')
    #     source_vertex = int(source_vertex)
    #     destination_vertex = input('Destination vertex: ')
    #     destination_vertex = int(destination_vertex)
    #     if self._graph.is_edge(source_vertex, destination_vertex):
    #         print('The given edge exists!')
    #     else:
    #         print('The given edge does not exist!')
    #
    # def in_degree_ui(self):
    #     vertex = input('Vertex: ')
    #     vertex = int(vertex)
    #     print('The in degree of the given vertex is ' + str(self._graph.get_in_degree(vertex)))
    #
    # def out_degree_ui(self):
    #     vertex = input('Vertex: ')
    #     vertex = int(vertex)
    #     print('The out degree of the given vertex is ' + str(self._graph.get_out_degree(vertex)))
    #
    # def parse_outbound_edges_ui(self):
    #     vertex = input('Vertex: ')
    #     vertex = int(vertex)
    #     if self._graph.get_out_degree(vertex) != 0:
    #         edges = self._graph.parse_out_edges(vertex)
    #         for edge in edges:
    #             print('Source vertex: ' + str(vertex) + ', Destination vertex: ' + str(edge))
    #     else:
    #         print('The given vertex has no outbound edges')
    #
    # def parse_inbound_edges_ui(self):
    #     vertex = input('Vertex: ')
    #     vertex = int(vertex)
    #     if self._graph.get_in_degree(vertex) != 0:
    #         edges = self._graph.parse_in_edges(vertex)
    #         for edge in edges:
    #             print('Destination vertex: ' + str(vertex) + ', Source vertex: ' + str(edge))
    #     else:
    #         print('The given vertex has no inbound edges!')
    #
    # def get_edge_cost_ui(self):
    #     source_vertex = input('Source vertex: ')
    #     source_vertex = int(source_vertex)
    #     destination_vertex = input('Destination vertex: ')
    #     destination_vertex = int(destination_vertex)
    #     print('The given edge cost is ' + str(self._graph.get_edge_cost(source_vertex, destination_vertex)))
    #
    # def modify_edge_cost_ui(self):
    #     source_vertex = input('Source vertex: ')
    #     source_vertex = int(source_vertex)
    #     destination_vertex = input('Destination vertex: ')
    #     destination_vertex = int(destination_vertex)
    #     newCost = input('New cost: ')
    #     newCost = int(newCost)
    #     self._graph.modify_edge_cost(source_vertex, destination_vertex, newCost)
    #     print('Cost modified successfully!')
    #
    # def add_edge_ui(self):
    #     source_vertex = input('Source vertex: ')
    #     source_vertex = int(source_vertex)
    #     destination_vertex = input('Destination vertex: ')
    #     destination_vertex = int(destination_vertex)
    #     cost = input('New cost: ')
    #     cost = int(cost)
    #     self._graph.add_edge(source_vertex, destination_vertex, cost)
    #     print('Edge added successfully!')
    #
    # def remove_edge_ui(self):
    #     source_vertex = input('Source vertex: ')
    #     source_vertex = int(source_vertex)
    #     destination_vertex = input('Destination vertex: ')
    #     destination_vertex = int(destination_vertex)
    #     self._graph.remove_edge(source_vertex, destination_vertex)
    #     print('Edge removed successfully!')
    #
    # def add_vertex_ui(self):
    #     self._graph.add_vertex()
    #     print('Vertex added successfully!')
    #
    # def remove_vertex_ui(self):
    #     vertex = input('Vertex to be removed: ')
    #     vertex = int(vertex)
    #     self._graph.remove_vertex(vertex)
    #     print('Vertex removed successfully!')
    #
    # def copy_graph_ui(self):
    #     print('Copy created successfully!')
    #     print(self._graph.is_edge(2,3))
    #     graph_copy = self._graph.copy_of_graph()
    #     print(graph_copy.is_edge(2,3))
    #     graph_copy.remove_vertex(2)
    #     print(graph_copy.is_edge(2,3))
    #     print(self._graph.is_edge(2,3))

    def read_graph_ui(self):
        read_graph(self._graph)
        self._graph.visited = self._graph.nr_of_vertices
        print('Graph read successfully!')

    # def write_graph_ui(self):
    #     write_graph(self._graph)
    #     print('Graph written successfully!')
    #
    # def create_random_graph(self):
    #     nr_of_vertices = input('Number of vertices: ')
    #     nr_of_vertices = int(nr_of_vertices)
    #     nr_of_edges = input('Number of edges: ')
    #     nr_of_edges = int(nr_of_edges)
    #     create_random_graph(self._graph, nr_of_vertices, nr_of_edges)
    #     self._graph.visited = self._graph.nr_of_vertices
    #     print('Random graph created successfully!')

    def print_graph(self):
        for index in self._graph.dictionaryOUT:
            for j in self._graph._dictionaryOUT[index]:
                print(str(index) + '->' + str(j))

    def connected_components_BF(self):
        connectedComponents = self._graph.connected_components()
        print('The undirected graph has ' + str(len(connectedComponents)) + ' connected components!')
        print('The connected components:')
        print(connectedComponents)

    def print_menu(self):
        print('\n\n')
        print('0. Exit;')
        # print('1. Get number of vertices;')
        # print('2. Parse the set of vertices;')
        # print('3. Find out if an edge exists;')
        # print('4. Get the in degree of a vertex;')
        # print('5. Get the out degree of a vertex;')
        # print('6. Parse the set of outbound edges of a vertex;')
        # print('7. Parse the set of inbound edges of a vertex;')
        # print('8. Get the cost of an edge;')
        # print('9. Modify the cost of an edge;')
        # print('10. Add a new edge;')
        # print('11. Remove an edge;')
        # print('12. Add a new vertex;')
        # print('13. Remove a vertex;')
        # print('14. Copy the graph;')
        print('15. Read the graph from a text file;')
        # print('16. Write the graph to a text file;')
        # print('17. Create a random graph;')
        print('18. Print the graph in the console;')
        print('19. Find the connected components of an undirected graph using breadth-first traversal of the graph.')
        print('\n\n')

    def start_program(self):
        # menuItems = {'0': self.exit_ui, '1': self.get_nr_of_vertices_ui, '2':self.parse_vertices_ui, '3': self.is_edge_ui, '4': self.in_degree_ui,
        #              '5': self.out_degree_ui, '6': self.parse_outbound_edges_ui, '7': self.parse_inbound_edges_ui, '8': self.get_edge_cost_ui,
        #              '9': self.modify_edge_cost_ui, '10': self.add_edge_ui, '11': self.remove_edge_ui, '12': self.add_vertex_ui, '13': self.remove_vertex_ui,
        #              '14': self.copy_graph_ui, '15': self.read_graph_ui, '16': self.write_graph_ui, '17': self.create_random_graph, '18': self.print_graph,
        #              '19': self.connected_components_BF}
        menuItems = {'0': self.exit_ui, '15': self.read_graph_ui, '18': self.print_graph, '19':self.connected_components_BF}

        while True:
            self.print_menu()
            option = input('Enter an option: ').strip().lower()
            try:
                if option in menuItems:
                    menuItems[option]()
                else:
                    print('This is not a command!')
            except GraphException as ge:
                print(ge)
