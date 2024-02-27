'''
首先，python中的字符串是不可变的，不可以通过下标来修改字符串

字符串可以直接通过加法来拼接
'''

def reverse_string(s):
    """
    反转字符串

    >>> reverse_string('hello')
    'olleh'
    >>> reverse_string('Python')
    'nohtyP'
    >>> reverse_string('')
    ''
    """
    return s[::-1]

def split_string(s, delimiter):
    """
    字符串切分 (非常重要)

    >>> split_string('apple,banana,orange', ',')
    ['apple', 'banana', 'orange']
    >>> split_string('hello world', ' ')
    ['hello', 'world']
    >>> split_string('one;two;three', ';')
    ['one', 'two', 'three']
    >>> split_string('hello', ',')
    ['hello']
    """
    return s.split(delimiter)

def custom_join(strings, delimiter):
    """
    字符串拼接 （重要）

    >>> custom_join(['apple', 'banana', 'orange'], ', ')
    'apple, banana, orange'
    >>> custom_join(['hello', 'world'], ' ')
    'hello world'
    >>> custom_join(['one', 'two', 'three'], ';')
    'one;two;three'
    >>> custom_join(['hello'], ', ')
    'hello'
    """
    return delimiter.join(strings)

def slice_string(s, start, end):
    """
    字符串切片

    >>> slice_string('hello world', 0, 5)
    'hello'
    >>> slice_string('hello world', 6, 11)
    'world'
    >>> slice_string('python', 1, 4)
    'yth'
    >>> slice_string('python', 2, 2)
    ''
    """
    return s[start:end]

if __name__ == '__main__':
    s = "a-b-c"
    b = s.split("-")
    print(b[0])
    print(b[1])
    print(b[2])
