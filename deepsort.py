def deep_sorted(x: any) -> str:
    """
    Returns a string representation of the sorted input data with deep sorting.

    >>> deep_sorted({"a": 5, "c": 6, "b": [1, 3, 2, 4]})
    '{"a": 5, "b": [1, 2, 3, 4], "c": 6}'

    >>> deep_sorted({"f": {"d": 1, "a": 2}})
    '{"f": {"a": 2, "d": 1}}'

    >>> deep_sorted({'a': 6, 'c': 7, 'b': [3, 6, [4, 9], 2, 7, 0]})
    '{"a": 6, "b": [0, 2, 3, 6, 7, [4, 9]], "c": 7}'

    >>> deep_sorted([5, {'a': 9, 'f': 7, 'b': 4}, (9, 8)])
    '[(8, 9), 5, {"a": 9, "b": 4, "f": 7}]'

    >>> deep_sorted([1, [2, 3], (4, 5), {6, 7}, 8, '9'])
    '[(4, 5), 1, 8, 9, [2, 3], {6, 7}]'

    >>> deep_sorted((9, (8, (7, (6, (5, (4, (3, (2, 1)))))))))
    '((((((((1, 2), 3), 4), 5), 6), 7), 8), 9)'

     >>> deep_sorted([{"r": 1, "a": 2}, {"t": 1, "b": 2}])
     '[{"a": 2, "r": 1}, {"b": 2, "t": 1}]'

     >>> deep_sorted((2,{"c": 1, "b": 2}))
     '(2, {"b": 2, "c": 1})'

     >>> deep_sorted([[[[[[[[9, 8], 7], 6], 5], 4], 3], 2], 1])
     '[1, [2, [3, [4, [5, [6, [7, [8, 9]]]]]]]]'

    >>> deep_sorted([{1,4,3}, {3,7,1}, {6,3,5}])
    '[{1, 3, 4}, {1, 3, 7}, {3, 5, 6}]'


    >>> deep_sorted([{1,4,3}, {"f": {"b": 1, "a": 2}, "d": 1}, (3,2)])
    '[(2, 3), {"d": 1, "f": {"a": 2, "b": 1}}, {1, 3, 4}]'

    >>> deep_sorted({"c" : {"b" : { "a" : 1}}})
    '{"c": {"b": {"a": 1}}}'

    >>> deep_sorted(([2,5,3], {8,4,5}))
    '([2, 3, 5], {4, 5, 8})'

    """
    if isinstance(x, dict):
        # sorted_dict = '{' + ', '.join(f"'{k}': {deep_sorted(v)}" for k, v in sorted(x.items())) + '}'
        sorted_dict = '{' + ', '.join(f'"{k}": {deep_sorted(v)}' for k, v in sorted(x.items())) + '}'
        return sorted_dict
    elif isinstance(x, (list, tuple, set)):
        if isinstance(x, set):
            sorted_set = sorted([deep_sorted(item) for item in x])
            return '{' + ', '.join(sorted_set) + '}'
        elif isinstance(x, tuple):
            sorted_tuple = tuple(sorted([deep_sorted(item) for item in x]))
            return '(' + ', '.join(sorted_tuple) + ')'
        else:
            sorted_list = sorted([deep_sorted(item) for item in x])
            return '[' + ', '.join(sorted_list) + ']'
    else:
        return str(x)


if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    x = eval(input())
    print(deep_sorted((x)))