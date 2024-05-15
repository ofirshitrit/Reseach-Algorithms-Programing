import random
import subprocess, sys
subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxpy"], stdout=subprocess.DEVNULL)
subprocess.check_call([sys.executable, "-m", "pip", "install", "cvxopt"], stdout=subprocess.DEVNULL)

import networkx as nx, cvxpy, numpy as np, matplotlib.pyplot as plt

def mincover(graph: nx.Graph)->int:
    """
    Find the minimum vertex cover size in the graph using integer linear programming

    :param graph: The input graph
    :return: A number containing the minimum vertex cover size

    >>> edges = [(0, 2), (1, 2)]
    >>> graph = nx.Graph(edges)
    >>> mincover(graph)
    1

    >>> edges = [(0, 2), (1, 2), (3,2), (3,1)]
    >>> graph = nx.Graph(edges)
    >>> mincover(graph)
    2

    >>> edges = [(0, 1), (2, 3), (4,5)]
    >>> graph = nx.Graph(edges)
    >>> mincover(graph)
    3

    >>> edges = [(0, 1), (0, 2), (1, 2)]
    >>> graph = nx.Graph(edges)
    >>> mincover(graph)
    2

    >>> edges = [(0, 1), (0, 2), (0, 3), (1,2), (1,3), (2,3)]
    >>> graph = nx.Graph(edges)
    >>> mincover(graph)
    3
    """
    # Number of nodes in the graph
    n = graph.number_of_nodes()

    # Decision variables: x[i] equals 1 if node i is in the vertex cover, 0 otherwise
    x = cvxpy.Variable(n, boolean=True)

    # Objective: minimize the sum of decision variables (i.e., minimize the size of the vertex cover)
    objective = cvxpy.Minimize(cvxpy.sum(x))

    # Constraints: for each edge (u, v), at least one of the nodes u or v must be in the vertex cover
    constraints = []
    for u, v in graph.edges:
        constraints.append(x[u] + x[v] >= 1)

    # Define the optimization problem
    problem = cvxpy.Problem(objective, constraints)

    # Solve the optimization problem
    problem.solve()

    # Return the integer value of the optimal objective function (rounded to the nearest integer)
    return int(np.round(problem.value))


def test_mincover():
    for i in range(10):
        num_nodes = random.randint(2, 50)
        num_edges = random.randint(1, 1000)
        graph = nx.gnm_random_graph(num_nodes, num_edges)
        min_cover_size = mincover(graph)
        print(f"Graph {i+1}:")
        print(f"Number of nodes: {num_nodes}")
        print(f"Number of arcs: {num_edges}")
        print(f"Minimum Vertex Cover Size: {min_cover_size}")
        print()


if __name__ == '__main__':
    edges=eval(input())
    graph = nx.Graph(edges)
    # plt.figure(figsize=(8, 6))
    # nx.draw(graph, with_labels=True, node_color='skyblue', node_size=800, font_size=12, font_weight='bold')
    # plt.show()
    print(mincover((graph)))
    # test_mincover()