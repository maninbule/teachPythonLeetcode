'''
给你两个字符串，表示两个单词，里面只包含小写字母

问这两个单词是否是异构的
异构的意思： 组成的元素是一样的，只是元素的顺序不同

input: "hello" "ohell"
output: true
input: "hello" "ohelt"
output: false
'''

def solve(s1:str,s2:str)->bool:
    from collections import defaultdict
    mp = defaultdict(int)
    for c in s1:
        mp[c] += 1
    for c in s2:
        mp[c] -= 1
    for key,value in mp.items():
        if value != 0:
            return False
    return True


s1 = "hello"
s2 = "ohell"
# output:true
print(solve(s1,s2))

s1 = "hello"
s2 = "ohelt"
# output:false
print(solve(s1,s2))

s1 = "aaa"
s2 = "aaaaa"
# output:false
print(solve(s1,s2))

s1 = ""
s2 = ""
# output:true
print(solve(s1,s2))

s1 = ""
s2 = "abc"
# output:false
print(solve(s1,s2))

s1 = "aabbb"
s2 = "aaabb"
# output:false
print(solve(s1,s2))