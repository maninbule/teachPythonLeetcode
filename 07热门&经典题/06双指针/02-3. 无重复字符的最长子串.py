'''
https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/?envType=study-plan-v2&envId=top-interview-150
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        ans = 0
        j = 0
        cnt = defaultdict(int)
        for i in range(len(s)): # [i : j]
            while j < len(s) and cnt[s[j]] == 0:
                cnt[s[j]] += 1
                j += 1
            ans = max(ans,j - i)
            cnt[s[i]] -= 1
        return ans
