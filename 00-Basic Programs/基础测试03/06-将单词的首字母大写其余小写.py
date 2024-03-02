

'''
06-将单词的首字母大写其余小写

给你一个单词，字母全是字母
将首字母大写，其余小写，然后返回
'''

def upperFirst(s:str)->str:
    ans = ""
    for i in range(len(s)):
        if i == 0:
            ans += s[i].upper()
        else:
            ans += s[i].lower()
    return ans

assert upperFirst("woRld") == 'World'
assert upperFirst("WoRld") == 'World'
assert upperFirst("W") == 'W'
assert upperFirst("gITHUB") == 'Github'
print("pass")