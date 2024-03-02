

'''
给你一个字符串列表，请将里面的字符串用-进行连接
'''

def strJoin(s:list[str])->str:
    # ans = ""
    # for i in range(len(s)):
    #     if i > 0:
    #         ans += "-" + s[i]
    #     else:
    #         ans += s[i]
    # return ans
    #--------------------第二种
    return "-".join(s)


assert strJoin(['a','b','c']) == 'a-b-c'
assert strJoin(['a']) == 'a'
assert strJoin(['abc','def']) == 'abc-def'
print("pass")