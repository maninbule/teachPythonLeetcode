# https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/description/


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import defaultdict
        ans = 0
        for i in range(len(s)):
            cnt = defaultdict(int)
            for j in range(i,len(s)):
                cnt[s[j]] += 1
                if cnt[s[j]] > 2:
                    break
                else:
                    ans = max(ans,j - i + 1)
        return ans




