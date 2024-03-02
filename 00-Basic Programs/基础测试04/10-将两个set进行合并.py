
'''
10-将两个set进行合并
'''

def mergeTwoset(st1:set,st2:set)->set:
    # st3 = set()
    # for v in st1:
    #     st3.add(v)
    # for v in st2:
    #     st3.add(v)
    # return st3
    #========第二种=========
    # for v in st2:
    #     st1.add(v)
    # return st1
    #========第三种============
    return st1.union(st2)


assert mergeTwoset({'a','b','c'},{'d','e','f'}) == {'a','b','c','d','e','f'}
print("pass")