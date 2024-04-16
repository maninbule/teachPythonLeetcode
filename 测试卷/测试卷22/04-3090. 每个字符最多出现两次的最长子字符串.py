# https://leetcode.cn/problems/maximum-length-substring-with-two-occurrences/description/


class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        from collections import defaultdict
        ans = 0
        for i in range(len(s)):
            mp = defaultdict(int)
            length = 0
            for j in range(i,len(s)):
                mp[s[j]] += 1
                if mp[s[j]] <= 2:
                    length += 1
                else:
                    break
            ans = max(ans,length)
        return ans



