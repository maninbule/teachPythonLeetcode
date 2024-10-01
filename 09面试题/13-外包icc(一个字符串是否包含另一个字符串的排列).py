'''

'''

'''
题目：一个字符串是否包含另一个字符串的某个排列

a = "agssfjks"
b = "fss"
输出：True

a = "agssfjks"
b = "abc"
输出：False
'''
from collections import defaultdict
def eq(a: defaultdict[int], b: defaultdict[int])->bool:
    print(a,b)
    for key in b.keys():
        if key not in a:
            return False
        if a[key] != b[key]:
            return False
    return True
# 一般的做法
# def solution(a:str,b:str)->bool:
#     lena,lenb = len(a),len(b)
#     if lena < lenb:
#         return False
#     cnt_b = defaultdict(int)
#     for x in b:
#         cnt_b[x] += 1
#     for i in range(lena - lenb + 1):
#         cnt_a = defaultdict(int)
#         for j in range(i,i + lenb):
#             cnt_a[a[j]] += 1
#         if eq(cnt_a,cnt_b):
#             return True
#     return False
# 最优解：使用双指针
def solution(a:str,b:str)->bool:
    lena,lenb = len(a),len(b)
    if lena < lenb:
        return False
    cnt_b = defaultdict(int)
    for x in b:
        cnt_b[x] += 1
    cnt_a = defaultdict(int)
    for i in range(lena):
        cnt_a[a[i]] += 1
        if i - lenb >=0:
            cnt_a[a[i-lenb]] -= 1
        if eq(cnt_a,cnt_b):
            return True
    return False

if __name__ == '__main__':
    print(solution("agssfjks","fss"))
    print(solution("agssfjks","abc"))