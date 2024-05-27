import networkx as nx
import matplotlib.pyplot as plt
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

    def display(self):
        G = nx.DiGraph()
        for edge in self.edges:
            G.add_edge(edge.from_vertex.name, edge.to_vertex.name, weight=edge.weight)

        pos = nx.spring_layout(G)
        edge_labels = {(edge.from_vertex.name, edge.to_vertex.name): edge.weight for edge in self.edges}
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=2000, font_size=10, font_weight='bold')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()


def output_as_dict(distances):
    return distances

def output_as_list(distances):
    return [(vertex.name, distance) for vertex, distance in distances.items()]



def run_tests():
    test_cases = [
        {
            "name": "Adjacency Matrix",
            "data": [
                [0, 1, 4, 0, 0, 0],
                [1, 0, 4, 2, 7, 0],
                [4, 4, 0, 3, 5, 0],
                [0, 2, 3, 0, 4, 6],
                [0, 7, 5, 4, 0, 7],
                [0, 0, 0, 6, 7, 0]
            ],
            "type": "matrix"
        },
        {
            "name": "Adjacency List",
            "data": {
                '0': [('1', 1), ('2', 4)],
                '1': [('0', 1), ('2', 4), ('3', 2), ('4', 7)],
                '2': [('0', 4), ('1', 4), ('3', 3), ('4', 5)],
                '3': [('1', 2), ('2', 3), ('4', 4), ('5', 6)],
                '4': [('1', 7), ('2', 5), ('3', 4), ('5', 7)],
                '5': [('3', 6), ('4', 7)]
            },
            "type": "list"
        }
    ]

    algorithms = {
        "Dijkstra": lambda graph, start: graph.dijkstra(start),
        "Bellman-Ford": lambda graph, start: graph.bellman_ford(start)
    }

    output_formats = {
        "Dict Output": output_as_dict,
        "List Output": output_as_list
    }

    for test_case in test_cases:
        graph = Graph()
        if test_case["type"] == "matrix":
            graph.from_adjacency_matrix(test_case["data"])
        elif test_case["type"] == "list":
            graph.from_adjacency_list(test_case["data"])

        # Display the graph structure using matplotlib
        print(f"Displaying {test_case['name']} Graph")
        graph.display()

        for algo_name, algo_func in algorithms.items():
            distances = algo_func(graph, '0')
            for output_name, output_func in output_formats.items():
                print(f"{test_case['name']} - {algo_name} - {output_name}")
                print(output_func(distances))

run_tests()

