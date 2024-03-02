
'''
09-删除set中的所有大写字母

给你一个set，里面有小写字母和大写字母
你需要删除set中的大写字母
然后返回set
'''

def removeAllUpperChar(st:set)->set:
    for ascii in range(ord('A'),ord('Z') + 1):
        c = chr(ascii)
        if c in st:
            st.remove(c)
    return st

st = {'A', 'a', 'B', 'c'}
st = removeAllUpperChar(st)
assert 'A' not in st
assert 'B' not in st
assert 'a' in st
assert 'c' in st
print("pass")