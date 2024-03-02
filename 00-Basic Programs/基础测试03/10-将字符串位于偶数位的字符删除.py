
'''
10-将字符串位于偶数位的字符删除

例如：
输入：abcd
输出：ac
'''

def removeEvenChar(s:str)->str:
    ans = ""
    for i in range(len(s)):
        if i % 2 == 0:
            ans += s[i]
    return ans

assert removeEvenChar("abcd") == 'ac'
assert removeEvenChar("abc") == 'ac'
assert removeEvenChar("ab") == 'a'
assert removeEvenChar("a") == 'a'
print("pass")