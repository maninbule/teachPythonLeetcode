''''''
'''
要求将数组中的最小值调整为1，最大值尽可能小，且保持数组中元素的相对顺序。
输出修改后的数组

input: [4,2,9,10,5,5,7]

output: [2,1,5,6,3,3,4]


思路：
先拷贝一份数组到组数B
对数组B进行排序
B = [2,4,5,5,7,9,10]
rank = 0
map = {}
2: rank = 1 map = {2: 1}
4: rank = 2 map = {2:1,4: 2}
5: rank = 3 map = {2:1,4: 2,5:3}
5: continue
7: rank = 4 map = {2:1,4: 2,5:3,7:4}
9: rank = 5 map = {2:1,4: 2,5:3,7:4,9:5}
10: rank = 6  map = {2:1,4: 2,5:3,7:4,9:5,10 : 6}

遍历input数组[4,2,9,10,5,5,7]
result = [2,1,5,6,3,3,4]
'''

def solution(A:list[int])->list[int]:
    B = [x for x in A]
    B.sort()
    curRank = 0
    rank = dict()
    for x in B:
        if x not in rank:
            curRank += 1
            rank[x] = curRank
    result = [0] * len(A)
    for i in range(len(A)):
        result[i] = rank[A[i]]
    return result

A = [4,2,9,10,5,5,7]
print(solution(A))