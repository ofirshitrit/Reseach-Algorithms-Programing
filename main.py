from typing import List, Tuple, Dict, Any, Union


# Define City type for better readability
City = Tuple[str, Union[Tuple[float, float], Dict[str, float]]]  # (name, (x_coordinate, y_coordinate) or distances)


def euclidean_distance(city1: Tuple[float, float], city2: Tuple[float, float]) -> float:
    """
    Calculates the Euclidean distance between two cities.

    Args:
        city1: Tuple containing coordinates of the first city.
        city2: Tuple containing coordinates of the second city.

    Returns:
        The Euclidean distance between the two cities.
    """
    x1, y1 = city1
    x2, y2 = city2
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def tsp_bruteforce(distances: Dict[Tuple[str, str], float], cities: List[str]) -> List[str]:
    """
    Solves the TSP using a brute-force algorithm.

    Args:
        distances: Dictionary containing distances between each pair of cities.
        cities: List of city names.

    Returns:
        A list representing the optimal order to visit the cities.
    """
    from itertools import permutations

    shortest_route = None
    min_distance = float('inf')

    for route in permutations(cities):
        distance = sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1))
        distance += distances[route[-1], route[0]]  # Return to the starting city
        if distance < min_distance:
            min_distance = distance
            shortest_route = route

    return shortest_route


def tsp_greedy(distances: Dict[Tuple[str, str], float], cities: List[str]) -> List[str]:
    """
    Solves the TSP using a greedy algorithm.

    Args:
        distances: Dictionary containing distances between each pair of cities.
        cities: List of city names.

    Returns:
        A list representing the order to visit the cities.
    """
    current_city = cities[0]  # Start from the first city
    unvisited_cities = set(cities[1:])
    route = [current_city]

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distances[current_city, city])
        route.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    route.append(cities[0])  # Return to the starting city
    return route


def solve_tsp(algorithm: str, input_type: str, output_type: str, cities: List[City]) -> Any:
    """
    Solves the TSP problem based on the specified algorithm and input/output types.

    Args:
        algorithm: Algorithm to use ('bruteforce' or 'greedy').
        input_type: Type of input ('distances' or 'coordinates').
        output_type: Type of output ('route' or 'length').
        cities: List of cities with names and coordinates or distances.

    Returns:
        The solution based on the specified input/output types.
    """
    distances = {}
    city_names = [city[0] for city in cities]

    if input_type == 'distances':
        for city1 in cities:
            for city2, distance in city1[1].items():
                distances[city1[0], city2] = distance
    elif input_type == 'coordinates':
        for i, city1 in enumerate(cities):
            for j, city2 in enumerate(cities):
                if i != j:
                    distances[city1[0], city2[0]] = euclidean_distance(city1[1], city2[1])

    if algorithm == 'bruteforce':
        route = tsp_bruteforce(distances, city_names)
    elif algorithm == 'greedy':
        route = tsp_greedy(distances, city_names)

    if output_type == 'route':
        return route
    elif output_type == 'length':
        total_distance = sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1))
        total_distance += distances[route[-1], route[0]]  # Return to the starting city
        return total_distance


if __name__ == "__main__":
    # Test all 8 combinations
    cities = [("A", (0, 0)), ("B", (1, 1)), ("C", (2, 2)), ("D", (3, 3))]

    for algorithm in ['bruteforce', 'greedy']:
        for input_type in ['distances', 'coordinates']:
            for output_type in ['route', 'length']:
                result = solve_tsp(algorithm, input_type, output_type, cities)
                print(f"Algorithm: {algorithm}, Input: {input}")
