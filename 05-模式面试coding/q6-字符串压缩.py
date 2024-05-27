'''
给你一个字符串s
把字符串相邻相同的字符进行压缩，变成字符 + 次数
如果次数为1的字符，就不用写

例如：
input: aabccdeee
output:a2bc2de3

input:aaaabbbbbc
output:a4b5c
'''
def solve(s:str)->str:
    if len(s) == 0:
        return ""
    ans = ""
    cnt = 1
    for i in range(1,len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            ans += s[i-1]
            if cnt > 1:
                ans += str(cnt)
            cnt = 1
    ans += s[-1]
    if cnt > 1:
        ans += str(cnt)
    return ans

print(solve("aabccdeee"))
print(solve("aaaabbbbbc"))
print(solve("aaaaa"))
print(solve("a"))
print(solve(""))
print(solve("abcde"))