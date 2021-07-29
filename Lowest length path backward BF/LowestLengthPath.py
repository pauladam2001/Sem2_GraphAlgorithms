from Graph import create_random_graph


def find_accessible_vertices_backwards(graph, end_vertex):
    if end_vertex not in graph.parse_vertices():
        raise ValueError("The end vertex is not in the graph.")

    visited = []
    queue = []
    next_vertex = {}
    distance_to_end = {}

    queue.append(end_vertex)
    visited.append(end_vertex)
    distance_to_end[end_vertex] = 0
    while len(queue) > 0:
        y = queue[0]
        queue = queue[1:]
        for edge in graph.parse_inbound_edges(y):
            if edge.source_id not in visited:
                visited.append(edge.source_id)
                queue.append(edge.source_id)
                distance_to_end[edge.source_id] = distance_to_end[y] + 1
                next_vertex[edge.source_id] = y

    return next_vertex


def find_minimum_length_path(graph, start_vertex, end_vertex):
    next_vertex = find_accessible_vertices_backwards(graph, end_vertex)

    if start_vertex not in next_vertex.keys():
        raise ValueError("There is no path from " + str(start_vertex) + " to " + str(end_vertex))

    path = [start_vertex]
    last_vertex = start_vertex
    reached_end = False
    while not reached_end:
        path.append(next_vertex[last_vertex])
        last_vertex = next_vertex[last_vertex]
        if path[-1] == end_vertex:
            reached_end = True

    return path


def main():
    random_graph = create_random_graph(5, 10)

    print("THE GRAPH:")
    for vertex in random_graph.parse_vertices():
        for edge in random_graph.parse_outbound_edges(vertex):
            print(edge)

    print("\n")
    next_vertex = find_accessible_vertices_backwards(random_graph, 1)
    print(next_vertex.keys())
    print("\n")

    path = find_minimum_length_path(random_graph, 1, 4)
    print(path)


main()