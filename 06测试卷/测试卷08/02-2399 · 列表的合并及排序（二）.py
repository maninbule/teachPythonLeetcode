'''
https://www.lintcode.com/problem/2399/?showListFe=true&page=2&problemTypeId=8&pageSize=50
'''

def sorting_connection(list_1: list, list_2: list) -> list:
    '''
    :param list_1: Input list one
    :param list_2: Input list two
    :return: Sorting the list after merging
    '''
    # -- write your code here --
    for x in list_2:
        list_1.append(x)
    list_1.sort()
    return list_1