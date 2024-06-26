'''
https://www.lintcode.com/problem/2134/?showListFe=true&page=4&problemTypeId=8&pageSize=50
'''

def get_len_of_list(list_a: list) -> int:
    """
    :param list_a: The first source list
    :return: A length of list_in
    """
    # --write your code here--
    return len(list_a)

def add_two_list(list_a: list, list_b: list) -> list:
    """
    :param list_a: The second source list
    :param list_b: The third source list
    :return: A list about the combination of list_a and list_b
    """
    # write your code here
    ans = []
    for x in list_a:
        ans.append(x)
    for x in list_b:
        ans.append(x)
    return ans

def repeat_list(list_a: list) -> list:
    """
    :param list_a: The first source list
    :return: A list about 3 times reputations of list_in
    """
    # write your code here
    ans = []
    for i in range(3):
        for x in list_a:
            ans.append(x)
    return ans


def is_in_list(value: str, list_a: list) -> bool:
    """
    :param value: The fourth source string
    :param list_a: The second source list
    :return: A bool whether value is in list_a
    """
    # write your code here
    for x in list_a:
        if value == x:
            return True
    return False

def iterate_list(list_a: list) -> list:
    """
    :param list_a: The second source list
    :return: A list about the initial character in each element of list_a
    """
    # write your code here
    ans = []
    for s in list_a:
        ans.append(s[0])
    return ans