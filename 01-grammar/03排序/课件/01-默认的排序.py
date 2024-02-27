'''
• sort()是列表内置的方法，没有返回值，是将列表排序,列表变化了
• sorted是全局内置的方法，有返回值，返回对可迭代序列排序后的新对象，但是原来的序列不变
'''
import doctest
def ascending_sort(arr):
    """
    从小到大排序

    >>> ascending_sort([1, 67, 2, 1, 4, 5, 90, 23])
    [1, 1, 2, 4, 5, 23, 67, 90]
    """
    arr.sort()
    return arr

def descending_sort(arr):
    """
    从大到小排序

    >>> descending_sort([1, 67, 2, 1, 4, 5, 90, 23])
    [90, 67, 23, 5, 4, 2, 1, 1]
    """
    arr.sort(reverse=True)
    return arr

