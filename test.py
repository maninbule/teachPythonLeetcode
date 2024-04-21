



def solve(s:str)->str:
    from collections import defaultdict
    cnt = defaultdict(int)
    for c in s:
        cnt[c] += 1
    ans_char = s[0]
    for char,times in cnt.items():
        if times > cnt[ans_char]:
            ans_char = char
    return ans_char

# 测试
s = "abbbcccc" # out = c
print(solve(s))
s = "abbbccc" # out = b or c
print(solve(s))

