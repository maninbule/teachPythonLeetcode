
'''
07判断一个字符串是否是回文串
'''
def judgePalindromeOrNot(s:str)->bool:
    L,R = 0,len(s)-1
    while L < R:
        if s[L] != s[R]:
            return False
        L += 1
        R -= 1
    return True

print(judgePalindromeOrNot("1212"))