
'''
08-统计字符串中每个字符出现了多少次

你需要返回一个defaultdict字典
'''

from collections import defaultdict
def countAllChar(s:str)-> defaultdict[int]:
    mp = defaultdict(int) # key    value -> int = 0
    for c in s:
        mp[c] += 1
    return mp

s = "abc124scsrc"
d = countAllChar(s)
assert d['a'] == 1
assert d['1'] == 1
assert d['s'] == 2
assert d['c'] == 3
assert d['2'] == 1
assert d['4'] == 1
print("pass")