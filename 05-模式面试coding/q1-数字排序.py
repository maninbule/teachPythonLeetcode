'''
给你一个数组list[int]
我们需要对这个数组中出现过的数字种类，进行一个排序，按照出现的次数进行排序

优先按照出现次数的大小，出现次数多的排在前面
如果次数一样多，就按照数字的大小进行从小到大排序

input = [1,1,10,10,11,12,55,55,55,44,44,2,3]
output: [55,1,10,44,2,3,11,12]
'''
def solve(arr:list[int])->list[int]:
    mp = {}
    for v in arr:
        if v in mp:
            mp[v] += 1
        else:
            mp[v] = 1
    A = []
    for v,times in mp.items():
        A.append([v,times])
    A.sort(key=lambda x:(-x[1],x[0]))
    ans = []
    for x in A:
        ans.append(x[0])
    return ans

input = [1,1,10,10,11,12,55,55,55,44,44,2,3]
# output: [55,1,10,44,2,3,11,12]
print(solve(input))