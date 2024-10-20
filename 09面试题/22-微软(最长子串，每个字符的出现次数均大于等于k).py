''''''

'''
给你一个字符串
从中找到一个最长的子串, 里面每一个字符都至少出现了k次
然后返回这个子串

input: s = "abcabca" k = 2
output: "abcabca"

input: s = "aabbccdaabbc" k = 2
output: "aabbcc"


input: s = "aabcdabc" k = 2
output: ""


abcabddeflffwefgbdbsd k = 2
a: >= 2
b: >= 2
c: == 1
d: >= 2
e: >= 2
f: >= 2
l: == 1
g: == 1
s: == 1
w: == 1
[ab] c [abddef] l [ff] w [ef] g [bdb] s [d]

abddef
[dd]
res = dd

'''
from collections import defaultdict
class Solution:
    def solution(self,s:str,k:int)->str:
        self.result = ""
        self.dfs(s,k)
        return self.result

    def dfs(self,s:str,k:int):
        count = defaultdict(int)
        for c in s:
            count[c] += 1
        left = -1
        right = -1
        tag = True # 表示没有找到分隔符，如果找到了就改成False
        for i in range(len(s)):
            if count[s[i]] >= k:
                if left == -1:
                    left = i
                right = i
            else:
                tag = False
                if left != -1 and right != -1:
                    self.dfs(s[left:right + 1],k)
                left = right = -1
        if tag == True:
            if len(s) > len(self.result):
                self.result = s
            return
        if left != -1 and right != -1:
            self.dfs(s[left:right + 1],k)

s = Solution()
print(s.solution("abcabca",2))
print(s.solution("aabbccdaabbc",2))
print(s.solution("abcabddeflffwefgbdbsd",2))

'''
时间复杂度： 最坏时间复杂度 O(n^2)  平均时间复杂度: O(nlogn)
空间复杂度： O(n)
'''
