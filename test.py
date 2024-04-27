


# "ab cA d  " ->"Ab Ca D  "

def solve(s:str)->str:
    cnt = 0
    ans = ""
    for c in s:
        if c == ' ':
            ans += c
        else:
            cnt += 1
            if cnt%2 == 1:
                ans += c.upper()
            else:
                ans += c.lower()
    return ans

input = "ab cA d  "
print(solve(input))