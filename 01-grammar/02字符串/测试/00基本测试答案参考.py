

def sum_numbers_in_string(s):
    """
    求出字符串里面出现的数，数与数之间用的空格隔开

    >>> sum_numbers_in_string('12 34 88 90')
    224
    >>> sum_numbers_in_string('1 2 3 4 5')
    15
    >>> sum_numbers_in_string('10 20 30')
    60
    """
    result = s.split(" ")  # ['12','34','88','90']
    sum = 0
    for s in result:
        sum += int(s)
    return sum




