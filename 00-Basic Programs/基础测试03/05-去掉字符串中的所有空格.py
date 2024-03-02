
'''
05-去掉字符串中的所有空格

保留字符串中的所有的非空格的字符


'''

def removeSpaceInStr(s:str)->str:
    ans = ""
    for c in s:
        if c != ' ':
            ans += c
    return ans

assert removeSpaceInStr("abc def") == "abcdef"
assert removeSpaceInStr(" abc def ") == "abcdef"
assert removeSpaceInStr("def") == "def"
assert removeSpaceInStr("   ") == ""
print("pass")