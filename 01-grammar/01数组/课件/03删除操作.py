def remove_element_by_index(arr:list, index):
    """
    Remove an element from the list by index.

    >>> remove_element_by_index([1, 2, 3, 4, 5], 2)
    [1, 2, 4, 5]

    >>> remove_element_by_index(['a', 'b', 'c', 'd', 'e'], 3)
    ['a', 'b', 'c', 'e']
    """
    arr.pop(index)
    return arr

def pop_last_element(arr:list):
    """
    Pop the last element from the list.

    >>> pop_last_element([1, 2, 3, 4, 5])
    5

    >>> pop_last_element(['a', 'b', 'c', 'd', 'e'])
    'e'
    """

    return arr.pop()

def get_sublist(arr:list, start:int, end:int):
    """
    Get a sublist from the list based on start and end indices.

    >>> get_sublist([1, 2, 3, 4, 5], 1, 3)
    [2, 3]

    >>> get_sublist(['a', 'b', 'c', 'd', 'e'], 0, 3)
    ['a', 'b', 'c']
    """
    return arr[start:end]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

