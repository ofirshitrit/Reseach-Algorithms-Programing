import heapq
from itertools import takewhile, islice
def sorted_subset_sums(S):

    """

    :param S:
    :return:

    >>> from itertools import takewhile, islice
    >>> for i in sorted_subset_sums([1,2,4]): print(i, end=", ")
    0, 1, 2, 3, 4, 5, 6, 7,

    >>> list(sorted_subset_sums([1,2,3]))
    [0, 1, 2, 3, 3, 4, 5, 6]

    >>> list(sorted_subset_sums([2,3,4]))
    [0, 2, 3, 4, 5, 6, 7, 9]

    >>> list(islice(sorted_subset_sums(range(100)),5))
    [0, 0, 1, 1, 2]

    >>> list(takewhile(lambda x:x<=6, sorted_subset_sums(range(1,100))))
    [0, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6]

    >>> list(zip(range(5), sorted_subset_sums(range(100))))
    [(0, 0), (1, 0), (2, 1), (3, 1), (4, 2)]

    >>> len(list(takewhile(lambda x:x<=1000, sorted_subset_sums(list(range(90,100)) + list(range(920,1000))))))
    1104
    """
    S = sorted(S)  # Ensure S is sorted to handle subsets in increasing order
    n = len(S)

    # Min-heap to store the sums, initialized with the sum of the empty subset
    heap = [(0, 0)]  # (current_sum, index)

    # A set to track visited (current_sum, index) pairs to avoid duplicates
    visited = set((0, 0))

    while heap:
        current_sum, idx = heapq.heappop(heap)
        yield current_sum

        # Generate new sums by adding subsequent elements from S
        for i in range(idx, n):
            new_sum = current_sum + S[i]
            new_pair = (new_sum, i + 1)
            if new_pair not in visited:
                heapq.heappush(heap, new_pair)
                visited.add(new_pair)
