




# defaultdict key:int, value:list[str]
def solve(arr:list[str])->list[str]:
    from collections import defaultdict
    mp = defaultdict(list[str])
    for s in arr:
        mp[len(s)].append(s)
    ans = []
    for key,value in mp.items(): # value = list[str]
        ans.append("".join(value))
    ans.sort(key=lambda x:len(x))
    return ans

# 测试
input = ['a','b','abc','xyz','d']
# output = ['abd','abcxyz']
print(solve(input))