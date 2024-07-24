# https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/description/


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        j = 0
        from collections import defaultdict
        cnt = defaultdict(int)
        ans = 0
        for i in range(len(s)): # 0 - n-1
            while j < len(s) and cnt[s[j]] + 1 <= 2:
                cnt[s[j]] += 1
                j += 1
            ans = max(ans,j - i)
            cnt[s[i]] -= 1
        return ans








