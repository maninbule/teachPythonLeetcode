
'''
07-取出字符串中的子串

给你一个字符串，让你取出对应下标区间[L,R]的子字符串
L和R是对应字符串的下标

'''

def getSubstr(s:str,L:int,R:int)->str:
    # ans = ""
    # for i in range(len(s)):
    #     if L <= i <= R:
    #         ans += s[i]
    # return ans
    # -----------------第二种
    # ans = ""
    # for i in range(L,R+1):
    #     ans += s[i]
    # return ans
    # ------------------第三种
    return s[L:R+1]


assert getSubstr("world",1,3) == "orl"
assert getSubstr("world",0,4) == "world"
assert getSubstr("world",2,2) == "r"
print("pass")

