import numpy as np
from scipy.optimize import root
import matplotlib.pyplot as plt
import time


def solve_with_root(a: np.ndarray, b: np.ndarray):
    """
    Find the solutions to the equation ax=b using scipy.optimize.root
    :param a: Matrix
    :param b: Vector
    :return: Solution to the equation: ax=b

    >>> a = np.array([[1, 2], [3, 4]])
    >>> b = np.array([5, 6])
    >>> solve_with_root(a, b)
    array([-4. ,  4.5])

    >>> a = np.array([[1,8], [1, 0]])
    >>> b = np.array([5,2])
    >>> solve_with_root(a, b)
    array([2.   , 0.375])

    >>> a = np.array([[1, 8, 3], [1, 0, 4], [4, 2, 3]])
    >>> b = np.array([5, 2, 4])
    >>> solve_with_root(a, b)
    array([0.50980392, 0.42156863, 0.37254902])

    >>> a = np.array([[0,0], [0, 0]])
    >>> b = np.array([0,0])
    >>> solve_with_root(a, b)
    array([0., 0.])
    """

    # The function that the program will solve - the fun parameter or root
    def equation(x):
        return np.dot(a, x) - b

    # The solution should be as the same size as the vector b
    x0 = np.zeros(len(b))
    result = root(equation, x0)

    if result.success:
        return result.x
    else:
        raise ValueError("Root finding failed: " + result.message)


def test_solve_with_root():
    num_tests = 5
    for _ in range(num_tests):
        n = np.random.randint(2, 6)
        a = np.random.rand(n, n)  # np.linalg.solve get only square matrices
        b = np.random.randn(n)

        # Solve using solve_with_root
        try:
            solution_root = solve_with_root(a, b)
        except ValueError as e:
            print(f"Error: {e}")
            continue

        # Solve using numpy.linalg.solve
        try:
            solution_numpy = np.linalg.solve(a, b)
        except np.linalg.LinAlgError as e:
            print(f"Error: {e}")
            continue

        # Compare solutions
        if not np.allclose(solution_root, solution_numpy):
            print("Test failed:")
            print("Matrix a:\n", a)
            print("Vector b:", b)
            print("Solution (solve_with_root):", solution_root)
            print("Solution (numpy.linalg.solve):", solution_numpy)
        else:
            print("Test passed")


def compare_solution_methods():
    input_sizes = list(range(1, 1001, 50))

    # Initialize lists to store average running times
    avg_time_solve_with_root = []
    avg_time_numpy_solve = []

    # Perform comparisons for each input size
    for size in input_sizes:
        # Generate random matrix 'a' and vector 'b'
        a = np.random.randn(size, size)
        b = np.random.randn(size)

        # Measure running time for solve_with_root
        start_time = time.time()
        solve_with_root(a, b)
        end_time = time.time()
        elapsed_time_solve_with_root = end_time - start_time
        avg_time_solve_with_root.append(elapsed_time_solve_with_root)

        # Measure running time for numpy.linalg.solve
        start_time = time.time()
        np.linalg.solve(a, b)
        end_time = time.time()
        elapsed_time_numpy_solve = end_time - start_time
        avg_time_numpy_solve.append(elapsed_time_numpy_solve)

    # Plot the results
    plt.figure(figsize=(10, 6))
    plt.plot(input_sizes, avg_time_solve_with_root, label='solve_with_root', marker='o')
    plt.plot(input_sizes, avg_time_numpy_solve, label='numpy.linalg.solve', marker='o')
    plt.xlabel('Input Size')
    plt.ylabel('Average Running Time (seconds)')
    plt.title('Performance Comparison of Solution Methods')
    plt.legend()
    plt.grid(True)
    plt.savefig("comparison.png")  # after you plot the graphs, save them to a file and upload it separately.
    plt.show()


if __name__ == '__main__':
    # put your code here
    # test_solve_with_root()
    compare_solution_methods()
    # a = np.array([[1, 2], [3, 4]])
    # b = np.array([5, 6])
    #
    # a = np.array([[1,8], [1, 0]])
    # b = np.array([5,2])

    # a = np.array([[1, 8, 3], [1, 0, 4], [4, 7, 5]])
    # b = np.array([1, 2, 3])
    # #
    # # # solution = solve_with_root(a, b)
    # # # print("root:", solution)
    # #
    # try:
    #     print("linalg:", np.linalg.solve(a, b))
    # except:
    #     print("An exception has occurred!")
