import heapq


def sorted_subset_sums(series):

    """
    A generator that yields the sums of all subsets of the input series in non-decreasing order.

    :param series: List of integers to find subset sums.
    :return: Yields sums of all subsets of the input list in sorted order.

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
    series = sorted(series)  # Ensure series is sorted to handle subsets in increasing order
    len_series = len(series)

    # Min-heap to store the sums, initialized with the sum of the empty subset
    heap = [(0, 0)]  # (current_sum, index)

    while heap:
        current_sum, idx = heapq.heappop(heap)
        yield current_sum

        # Generate new sums by adding subsequent elements from S
        for i in range(idx, len_series):
            new_sum = current_sum + series[i]
            new_pair = (new_sum, i + 1)
            heapq.heappush(heap, new_pair)



if __name__ == '__main__':
    from itertools import takewhile, islice
    for i in eval(input()):
        print(i, end=", ")
