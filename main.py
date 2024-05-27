class Vertex:
    _instances = {}

    def __new__(cls, name):
        if name not in cls._instances:
            cls._instances[name] = super(Vertex, cls).__new__(cls)
            cls._instances[name].name = name
        return cls._instances[name]

    def __repr__(self):
        return f"Vertex({self.name})"

class Edge:
    def __init__(self, from_vertex, to_vertex, weight):
        self.from_vertex = from_vertex
        self.to_vertex = to_vertex
        self.weight = weight

    def __repr__(self):
        return f"Edge(from={self.from_vertex}, to={self.to_vertex}, weight={self.weight})"



class Graph:
    def __init__(self):
        self.vertices = {}
        self.edges = []

    def add_edge(self, from_vertex, to_vertex, weight):
        from_v = Vertex(from_vertex)
        to_v = Vertex(to_vertex)
        self.edges.append(Edge(from_v, to_v, weight))
        if from_v not in self.vertices:
            self.vertices[from_v] = []
        self.vertices[from_v].append((to_v, weight))

    def from_adjacency_matrix(self, matrix):
        for i, row in enumerate(matrix):
            for j, weight in enumerate(row):
                if weight != 0:
                    self.add_edge(str(i), str(j), weight)

    def from_adjacency_list(self, adj_list):
        for from_vertex, edges in adj_list.items():
            for to_vertex, weight in edges:
                self.add_edge(from_vertex, to_vertex, weight)

    def dijkstra(self, start_vertex):
        import heapq
        start_v = Vertex(start_vertex)
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_v] = 0
        pq = [(0, start_v)]

        while pq:
            current_distance, current_vertex = heapq.heappop(pq)

            if current_distance > distances[current_vertex]:
                continue

            for neighbor, weight in self.vertices.get(current_vertex, []):
                distance = current_distance + weight

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(pq, (distance, neighbor))

        return distances

    def bellman_ford(self, start_vertex):
        start_v = Vertex(start_vertex)
        distances = {vertex: float('inf') for vertex in self.vertices}
        distances[start_v] = 0

        for _ in range(len(self.vertices) - 1):
            for edge in self.edges:
                if distances[edge.from_vertex] + edge.weight < distances[edge.to_vertex]:
                    distances[edge.to_vertex] = distances[edge.from_vertex] + edge.weight

        for edge in self.edges:
            if distances[edge.from_vertex] + edge.weight < distances[edge.to_vertex]:
                raise ValueError("Graph contains a negative-weight cycle")

        return distances


def output_as_dict(distances):
    return distances

def output_as_list(distances):
    return [(vertex.name, distance) for vertex, distance in distances.items()]



def run_tests():
    adj_matrix = [
        [0, 1, 4, 0, 0, 0],
        [1, 0, 4, 2, 7, 0],
        [4, 4, 0, 3, 5, 0],
        [0, 2, 3, 0, 4, 6],
        [0, 7, 5, 4, 0, 7],
        [0, 0, 0, 6, 7, 0]
    ]

    adj_list = {
        '0': [('1', 1), ('2', 4)],
        '1': [('0', 1), ('2', 4), ('3', 2), ('4', 7)],
        '2': [('0', 4), ('1', 4), ('3', 3), ('4', 5)],
        '3': [('1', 2), ('2', 3), ('4', 4), ('5', 6)],
        '4': [('1', 7), ('2', 5), ('3', 4), ('5', 7)],
        '5': [('3', 6), ('4', 7)]
    }

    graph = Graph()
    graph.from_adjacency_matrix(adj_matrix)
    dijkstra_distances_matrix = graph.dijkstra('0')
    bellman_ford_distances_matrix = graph.bellman_ford('0')

    graph = Graph()
    graph.from_adjacency_list(adj_list)
    dijkstra_distances_list = graph.dijkstra('0')
    bellman_ford_distances_list = graph.bellman_ford('0')

    print("Adjacency Matrix - Dijkstra - Dict Output")
    print(output_as_dict(dijkstra_distances_matrix))

    print("Adjacency Matrix - Dijkstra - List Output")
    print(output_as_list(dijkstra_distances_matrix))

    print("Adjacency Matrix - Bellman-Ford - Dict Output")
    print(output_as_dict(bellman_ford_distances_matrix))

    print("Adjacency Matrix - Bellman-Ford - List Output")
    print(output_as_list(bellman_ford_distances_matrix))

    print("Adjacency List - Dijkstra - Dict Output")
    print(output_as_dict(dijkstra_distances_list))

    print("Adjacency List - Dijkstra - List Output")
    print(output_as_list(dijkstra_distances_list))

    print("Adjacency List - Bellman-Ford - Dict Output")
    print(output_as_dict(bellman_ford_distances_list))

    print("Adjacency List - Bellman-Ford - List Output")
    print(output_as_list(bellman_ford_distances_list))

run_tests()
