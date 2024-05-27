'''
https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        from collections import defaultdict
        cnt = defaultdict(int)
        j = 0
        ans = 0
        for i in range(len(s)):
            while j < len(s) and cnt[s[j]] == 0:
                cnt[s[j]] += 1
                j += 1
            ans = max(ans,j - i)
            cnt[s[i]] -= 1
        return ans