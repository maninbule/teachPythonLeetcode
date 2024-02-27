'''
常用的两个函数是：
字符转ascii码： ascii = ord('a')
ascii码转字符： c = chr(ascii)

什么是ASCII
计算机是以数字形式存储一切数据的，那么我们就想要知道字符是怎么样存储的。
其实在计算机中是把字符做了一个映射，把常见的字符都映射成了0~127了，我们只管常见的字符是怎么编码的就好，不常用的字符我们就不去了解。
ASCII字符对照：https://baijiahao.baidu.com/s?id=1704767913015693638&wfr=spider&for=pc
ASCII在我们编程中有什么作用呢？
例子
假如我们现在手上有一个字母，我们想知道这个字母的下一个字母是谁？
如果我们不知道ASCII，我们就只能通过枚举来输出他的下一个字母
x = input()
if x == 'a': print("b");
if x == 'b': print("c");
if x == 'c': print("d");
...
...
...

但是我们知道了ASCII之后，我们就知道字母的ASCII是连续的，假如一个字母的ASCII码是x，那么它下一个字母的ASCII码就是x + 1
所以上面的代码就可以改成下面这样
'''

def asciiToChar(c:str)->str:
    '''
    >>> asciiToChar('a')
    'b'
    >>> asciiToChar('c')
    'd'
    >>> asciiToChar('A')
    'B'
    >>> asciiToChar('t')
    'u'
    '''
    return chr(ord(c)+1)

'''
字符当数字来用（考的很少，但是要知道）
既然字符使用的ASCII码，他的范围是0-127，那么我们是否可以直接把他当小范围的整数类型用呢？
答案是可以的，但是使用的范围是比较局限的，常见的就是统计字符出现的次数，把ASCII作为数组的下标

一般这种只会作为哈希表的优化来考察
'''

def charToASCII(s:str)->str:
    '''
    >>> charToASCII('hello')
    ' e 1 h 1 l 2 o 1'

    >>> charToASCII('Python')
    ' P 1 h 1 n 1 o 1 t 1 y 1'

    >>> charToASCII('')
    ''

    >>> charToASCII('aabbcc')
    ' a 2 b 2 c 2'
    '''
    cnt = [0] * 128
    for c in s:
        ascii = ord(c)
        cnt[ascii] += 1
    ans = ""
    for ascii in range(128):
        if cnt[ascii] > 0:
            ans += " " + chr(ascii) + " " + str(cnt[ascii])
    return ans


if __name__ == '__main__':

    print(ord('a'))

    print(chr(98))

