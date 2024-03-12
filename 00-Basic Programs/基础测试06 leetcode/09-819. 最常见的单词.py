
'''
url: https://leetcode.cn/problems/most-common-word/description/
'''
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        from collections import defaultdict
        cnt = defaultdict(int)
        st = set()
        for word in banned:
            st.add(word.lower())
        paragraph2 = ""
        for c in paragraph:
            if c.isalpha():
                paragraph2 += c.lower()
            else:
                paragraph2 += ' '
        words = paragraph2.split()
        for w in words:
            if w in st:
                continue
            cnt[w] += 1
        ans,maxtimes = "",0
        for word,times in cnt.items():
            if times > maxtimes:
                maxtimes = times
                ans = word
        return ans

'A,b C d F'
"a b c d f"