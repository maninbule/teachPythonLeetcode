'''
https://leetcode.cn/problems/substrings-of-size-three-with-distinct-characters/description/
'''

class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(2,len(s)):
            st = set()
            # st.add(s[i-2])
            # st.add(s[i-1])
            # st.add(s[i])
            st = set(s[i-2:i+1]) # s[0,2] => [i-2,i+1]
            if len(st) == 3:
                ans += 1
        return ans
