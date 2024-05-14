'''

给你一个数组，你需要进行删除重复的数字，对于有重复的数字，只保留最后一次出现的对应数字

input: [1, 2, 3, 3, 5, 2]
output: [1,3,5,2]

input: [1,2,2,1]
output: [2,1]
'''

def solve(arr:list[int])->list[int]:
    vis = set()
    ans = []
    for i in range(len(arr)-1,-1,-1):
        if arr[i] in vis:
            continue
        ans.append(arr[i])
        vis.add(arr[i])
    return ans[::-1]

input = [1,2,3,3,5,2]
print(solve(input))

input = [1,2,2,1]
print(solve(input))

