
'''
05-去掉字符串中的所有空格
'''

def removeSpaceInStr(s:str)->str:
    pass

assert removeSpaceInStr("abc def") == "abcdef"
assert removeSpaceInStr(" abc def ") == "abcdef"
assert removeSpaceInStr("def") == "def"
assert removeSpaceInStr("   ") == ""