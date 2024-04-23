


def solve(s:str)->str:
    ans = ""
    cur = ""
    for c in s:
        if c.isalpha():
            cur += c
        else:
            if len(cur) > 0:
                ans += cur[::-1]
                cur = ""
            ans += c
    if len(cur) > 0:
        ans += cur[::-1]
    return ans

s = "hello   world code" # output: olleh   dlrow edoc
print(solve(s))