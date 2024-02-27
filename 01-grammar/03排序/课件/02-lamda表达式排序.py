

def sort_ascending(arr):
    """
    Sort the given list in ascending order.

    >>> sort_ascending([1, 67, 2, 1, 4, 5, 90, 23])
    [1, 1, 2, 4, 5, 23, 67, 90]
    """
    arr.sort(key=lambda x: x)
    return arr

def sort_descending(arr):
    """
    Sort the given list in descending order.

    >>> sort_descending([1, 67, 2, 1, 4, 5, 90, 23])
    [90, 67, 23, 5, 4, 2, 1, 1]
    """
    arr.sort(key=lambda x: -x)
    return arr

def sort_tuple_ascending(lst):
    """
    Sort the given list of tuples in ascending order based on the first element.

    >>> sort_tuple_ascending([(9, 4), (2, 10), (4, 3), (3, 6)])
    [(2, 10), (3, 6), (4, 3), (9, 4)]
    """
    lst.sort(key=lambda item: item[0])
    return lst

def sort_tuple_custom(lst):
    """
    Sort the given list of tuples based on custom criteria.

    >>> sort_tuple_custom([(2, 4), (2, 10), (3, 3), (3, 6)])
    [(2, 10), (2, 4), (3, 6), (3, 3)]
    """
    lst.sort(key=lambda item: (item[0], -item[1]))
    return lst