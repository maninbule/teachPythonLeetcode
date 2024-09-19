'''
https://leetcode.cn/problems/longest-substring-without-repeating-characters/
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        left = 0
        res = 0
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left += 1
            st.add(s[right])
            # 区间就是[left,right]这一段
            res = max(res,right - left + 1)
        return res

# 输出不重复子串的具体字符串，而不是只是长度

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st = set()
        left = 0
        res = 0
        res_str = ""
        for right in range(len(s)):
            while s[right] in st:
                st.remove(s[left])
                left += 1
            st.add(s[right])
            # 区间就是[left,right]这一段
            if right - left + 1 > res:
                res = max(res,right - left + 1)
                res_str = s[left:right + 1]
        return res_str
