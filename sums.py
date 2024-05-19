# Put your iterator/generator here.
# It should be called: sorted_subset_sums.
import itertools
import heapq


def sorted_subset_sums(series):
    """
       Generate the sorted sums of all subsets of the input series.

       :param series: list of different positive numbers.
       yields: The sum of each subset in ascending order.

        >>> from itertools import takewhile, islice

       # >>> for i in sorted_subset_sums([1,2,4]): print(i, end=", ")
       # 0, 1, 2, 3, 4, 5, 6, 7,

        >>> list(sorted_subset_sums([1,2,3]))
        [0, 1, 2, 3, 3, 4, 5, 6]

        >>> list(sorted_subset_sums([2,3,4]))
        [0, 2, 3, 4, 5, 6, 7, 9]

        >>> list(takewhile(lambda x:x<=6, sorted_subset_sums(range(1,100))))
        [0, 1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6]

        >>> list(zip(range(5), sorted_subset_sums(range(100))))
        [(0, 0), (1, 0), (2, 1), (3, 1), (4, 2)]



    """
    series = sorted(series)

    def generate_subsets(index, current_sum):
        if index == len(series):
            yield current_sum
            return

        # Include the current element in the subset
        yield from generate_subsets(index + 1, current_sum + series[index])

        # Exclude the current element from the subset
        yield from generate_subsets(index + 1, current_sum)

    yield from generate_subsets(0, 0)


if __name__ == '__main__':
    from itertools import takewhile, islice
    # for i in eval(input()):
    #     print(i, end=", ")
    # j = 0
    for i in sorted_subset_sums(range(100)):
        print(f"Current subset sum: {i} ")
        # print(i, end=", ")
    # print(list(islice(sorted_subset_sums(range(100)), 5)))

    print(list(takewhile(lambda x: x <= 6, sorted_subset_sums(range(1, 100)))))