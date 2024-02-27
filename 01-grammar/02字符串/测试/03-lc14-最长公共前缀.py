'''
url:https://leetcode.cn/problems/longest-common-prefix/description/
如果有疑问直接写在这个当前文件，并标注不懂的地方
'''
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = ""
        for i in range(len(strs[0])): # strs[0]
            c = strs[0][i]
            for j in range(1,len(strs)): # strs[1],strs[2]
                if i >= len(strs[j]) or c != strs[j][i]:
                    return pre
            pre += c
        return pre