'''
https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        st = set()
        j = 0
        res = 0
        for i in range(n):
            while j < n and s[j] not in st: # 不重复就一直走
                st.add(s[j])
                j += 1
            # j就处于一个重复的位置，或者已经越界了
            # 以i为左端点，右端点j刚好走到此时的位置，就重复了，或者已经越界了
            res = max(res, j - i)
            # i要换成i + 1了，要从st中删除掉下标i的元素
            st.remove(s[i])
        return res
