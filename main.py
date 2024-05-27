from typing import List, Dict, Tuple, Union
import heapq
import random

# Define input types
GraphType1 = Dict[int, List[Tuple[int, int]]]  # Adjacency List
GraphType2 = List[List[Union[int, float]]]     # Adjacency Matrix

# Define output types
PathType1 = List[int]   # List of vertices representing the shortest path
PathType2 = int         # Length of the shortest path

# Define algorithms
def dijkstra(graph: Union[GraphType1, GraphType2], start: int) -> Tuple[Union[PathType1, PathType2]]:
    """
    Dijkstra's algorithm to find the shortest path from a starting vertex to all other vertices.

    Args:
    - graph: The graph representation (either adjacency list or adjacency matrix).
    - start: The starting vertex.

    Returns:
    - If output type is PathType1: A tuple containing the shortest path (list of vertices) and the shortest path length.
    - If output type is PathType2: The length of the shortest path.
    """
    # Implementation of Dijkstra's algorithm
    if isinstance(graph, GraphType1):
        # Implement Dijkstra's algorithm for adjacency list representation
        pass
    elif isinstance(graph, GraphType2):
        # Implement Dijkstra's algorithm for adjacency matrix representation
        pass
    else:
        raise ValueError("Invalid graph type")

def bfs(graph: Union[GraphType1, GraphType2], start: int) -> Tuple[Union[PathType1, PathType2]]:
    """
    Breadth-First Search (BFS) to find the shortest path from a starting vertex to all other vertices.

    Args:
    - graph: The graph representation (either adjacency list or adjacency matrix).
    - start: The starting vertex.

    Returns:
    - If output type is PathType1: A tuple containing the shortest path (list of vertices) and the shortest path length.
    - If output type is PathType2: The length of the shortest path.
    """
    # Implementation of BFS
    if isinstance(graph, GraphType1):
        # Implement BFS for adjacency list representation
        pass
    elif isinstance(graph, GraphType2):
        # Implement BFS for adjacency matrix representation
        pass
    else:
        raise ValueError("Invalid graph type")

# Test and demonstrate the system on all 8 combinations
def test_system():
    # Test cases for different combinations of input types, output types, and algorithms
    for input_type in [GraphType1, GraphType2]:
        for output_type in [PathType1, PathType2]:
            for algorithm in [dijkstra, bfs]:
                # Create a sample graph
                graph = create_sample_graph(input_type)

                # Choose a starting vertex
                start_vertex = choose_start_vertex(graph)

                # Find shortest path using the selected algorithm
                shortest_path = algorithm(graph, start_vertex)

                # Output the result based on the selected output type
                output_result(shortest_path, output_type)

def create_sample_graph(graph_type: Union[GraphType1, GraphType2]) -> Union[GraphType1, GraphType2]:
    """
    Function to create a sample graph based on the specified graph type.
    """
    if graph_type == GraphType1:
        # Sample graph in adjacency list representation
        sample_graph = {
            0: [(1, 5), (2, 3)],
            1: [(0, 5), (2, 2), (3, 6)],
            2: [(0, 3), (1, 2), (3, 7)],
            3: [(1, 6), (2, 7)]
        }
    elif graph_type == GraphType2:
        # Sample graph in adjacency matrix representation
        sample_graph = [
            [0, 5, 3, float('inf')],
            [5, 0, 2, 6],
            [3, 2, 0, 7],
            [float('inf'), 6, 7, 0]
        ]
    else:
        raise ValueError("Invalid graph type")
    return sample_graph

def choose_start_vertex(graph: Union[GraphType1, GraphType2]) -> int:
    """
    Function to choose a random starting vertex from the graph.
    """
    if isinstance(graph, GraphType1):
        # For adjacency list representation, choose a random key from the dictionary
        return random.choice(list(graph.keys()))
    elif isinstance(graph, GraphType2):
        # For adjacency matrix representation, choose a random index from the list
        return random.randint(0, len(graph) - 1)
    else:
        raise ValueError("Invalid graph type")

def output_result(shortest_path: Tuple[Union[PathType1, PathType2]], output_type: Union[PathType1, PathType2]):
    """
    Function to output the result based on the selected output type.
    """
    if isinstance(output_type, PathType1):
        if isinstance(shortest_path[0], list):
            print("Shortest path:", shortest_path[0])
            print("Shortest path length:", shortest_path[1])
        else:
            print("Shortest path:", shortest_path[0])
    elif isinstance(output_type, PathType2):
        print("Shortest path length:", shortest_path)
    else:
        raise ValueError("Invalid output type")

# Run the test system
test_system()
