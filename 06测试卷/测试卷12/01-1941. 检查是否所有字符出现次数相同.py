'''
https://leetcode.cn/problems/check-if-all-characters-have-equal-number-of-occurrences/description/
'''


class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        from collections import defaultdict
        cnt = defaultdict(int)
        for c in s:
            cnt[c] += 1
        # 计数完成了
        # times = cnt[s[0]]
        # for c in s:
        #     if times != cnt[c]:
        #         return False
        # return True
        st = set()
        for c in s:
            st.add(cnt[c])
        return len(st) == 1