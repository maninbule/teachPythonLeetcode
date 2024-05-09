

'''
给你一个字符串，里面包含空格，由小写字母组成的单词

你需要把所有的单词都翻转，并且保留空格，空格个数要一致

Input:  "  abc  defg h   "
output: "  cba  gfed h   "

Input:  "  abc  defg hi"
output: "  cba  gfed ih"
'''

def solve(s:str)->str:
    ans = ""
    word = ""
    for c in s:
        if c == ' ':
            if len(word) > 0:
                ans += word[::-1]
                word = ""
            ans += c
        else:
            word += c
    if len(word) > 0:
        ans += word[::-1]
    return ans

input = "  abc  defg hi" # output: "  cba  gfed ih"
print(solve(input))

